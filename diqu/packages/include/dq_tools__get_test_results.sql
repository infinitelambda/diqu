/* Get the the test result of the last 14 days */
with

source as (
    select * from @database.@schema.dq_issue_log
),

test_results_last_14_days as (
    select  *
            ,concat(
                coalesce(nullif(split(table_name,'.')[2],''),'-'),'|',
                coalesce(nullif(column_name,''),'-'),'|',
                coalesce(nullif(split(ref_table,'.')[2],''),'-'),'|',
                coalesce(nullif(ref_column,''),'-'),'|',
                test_unique_id
            ) as test_id
            ,case
                when no_of_records_failed > 0 and severity = 'error' then 'failed'
                when no_of_records_failed > 0 and severity = 'warn' then 'warn'
                else 'pass'
            end as test_status
            ,case
                when test_status = 'failed' then '🔴'
                when test_status = 'warn' then '🟡'
                else '✅'
            end as test_status_emoji

    from    source
    where   true
        --exclude dq-tools models
        and table_name not ilike '%bi_column_analysis%'
        and table_name not ilike '%bi_dq_metrics%'
        and table_name not ilike '%test_coverage%'
        --time limited to the last 14 days
        and check_timestamp > dateadd(day, -14, sysdate())
),

latest_status as (

    select  test_id
            ,test_status
            ,test_status_emoji
            ,check_timestamp
            ,no_of_records_scanned
            ,no_of_records_failed
            ,dq_issue_type
            ,kpi_category

    from    test_results_last_14_days

    qualify row_number() over (partition by test_id order by check_timestamp desc) = 1

),

prev_statuses as (

    select  test_id
            ,array_agg(test_status_emoji) within group (order by check_timestamp desc) as prev_statuses
            ,array_agg(check_timestamp) within group (order by check_timestamp desc) as prev_check_timestamps
            ,array_agg(no_of_records_scanned) within group (order by check_timestamp desc) as prev_no_of_records_scanned
            ,array_agg(no_of_records_failed) within group (order by check_timestamp desc) as prev_no_of_records_failed

    from    test_results_last_14_days

    group by test_id

)

select      concat(
                latest_status.test_status_emoji, ': ',
                latest_status.test_id,
                ' [$filter]'
            ) as jira_ticket_summary
            ,latest_status.test_id
            ,case
                when datediff(day, latest_status.check_timestamp, sysdate()) >=3 then 'deprecated'
                else latest_status.test_status
            end as test_status
            ,latest_status.test_status_emoji
            ,latest_status.check_timestamp
            ,latest_status.no_of_records_scanned
            ,latest_status.no_of_records_failed
            ,latest_status.no_of_records_failed / nullif(latest_status.no_of_records_scanned, 0) as failed_rate
            ,latest_status.dq_issue_type
            ,latest_status.kpi_category
            ,prev_statuses.prev_statuses
            ,prev_statuses.prev_check_timestamps
            ,prev_statuses.prev_no_of_records_scanned
            ,prev_statuses.prev_no_of_records_failed
            ,1 as priority --IMPORTANT: use your own logic to define the Priority

from        latest_status
left join   prev_statuses using (test_id)

order by    priority
