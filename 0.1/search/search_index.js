var __index = {"config":{"lang":["en"],"separator":"[\\s\\-,:!=\\[\\]()\"`/]+|\\.(?!\\d)|&[lg]t;|(?!\\b)(?=[A-Z][a-z])","pipeline":["stopWordFilter"]},"docs":[{"location":"index.html","title":"diqu","text":"<p>CLI companion tool supporting the Alert / Notification for  and more.</p>"},{"location":"index.html#installation","title":"Installation","text":"pip install diqu --upgrade Successfully installed diqu restart \u21bb <p>\ud83d\udcd3 NOTE: The DWH module should get installed already if you use <code>diqu</code> in a dbt project, if not, please perform additional step, for example, to install snowflake module:</p> <pre><code>pip install \"snowflake-connector-python[pandas]\"\npip install \"snowflake-connector-python[secure-local-storage]\"\n</code></pre>"},{"location":"index.html#usage","title":"Usage","text":"<pre><code>dbt run -s dq_tools # optional\ndiqu alert --to jira\n</code></pre> Sample logs <pre><code>04:33:17  diqu: INFO - Run with diqu==1.0.0 \ud83c\udfc3\n04:33:19  diqu: INFO - Using dbt project at: /path/to/dbt/project\n04:33:19  diqu: INFO - Using dbt profiles.yml at: ~/.dbt\n04:33:19  diqu: INFO - Using snowflake connection\n04:33:19  diqu: INFO - Looking for the query in: /path/to/file.sql\n04:33:23  diqu: INFO - Alerting to channel: JIRA\n04:33:23  diqu: INFO - \u2705 Done &gt; JIRA\n</code></pre> <p>In particular to the alert module, here are the additional configurations:</p> <ul> <li>For SLACK, you need to use the environment variables to configure the Slack Channel:</li> </ul> <pre><code>export SLACK_TOKEN=your_token\nexport SLACK_CHANNEL=your_channel_name\ndiqu alert --to slack\n</code></pre> <ul> <li>For JIRA, you need to use the environment variables to configure the JIRA Board:</li> </ul> <pre><code>export JIRA_SERVER=your_jira_server e.g. https://your_value.atlassian.net/\nexport JIRA_AUTH_USER=your_service_account e.g. dqt_user@your_value.com\nexport JIRA_AUTH_PASSWORD=your_service_token e.g. ATATTxxxxx\nexport JIRA_PROJECT_ID=your_project_id e.g. 106413\nexport JIRA_INCIDENT_TICKET_TYPE=your_ticket_type, default to \"[System] Incident\"\nexport JIRA_OPEN_TICKETS_FILTER=your_ticket_filter_on_title, default to \"*dq_tools\"\ndiqu alert --to jira\n</code></pre>"},{"location":"index.html#how-to-contribute","title":"How to Contribute","text":"<p>\ud83d\udc49 See CONTRIBUTING.md</p>"},{"location":"index.html#about-infinite-lambda","title":"About Infinite Lambda","text":"<p>Infinite Lambda is a cloud and data consultancy. We build strategies, help organisations implement them and pass on the expertise to look after the infrastructure.</p> <p>We are an Elite Snowflake Partner, a Platinum dbt Partner and two-times Fivetran Innovation Partner of the Year for EMEA.</p> <p>Naturally, we love exploring innovative solutions and sharing knowledge, so go ahead and:</p> <p>\ud83d\udd27 Take a look around our Git</p> <p>\u270f\ufe0f Browse our tech blog</p> <p>We are also chatty, so:</p> <p>\ud83d\udc40 Follow us on LinkedIn</p> <p>\ud83d\udc4b\ud83c\udffc Or just get in touch</p> <p></p>"},{"location":"nav/dev/contributing.html","title":"Contributing to <code>diqu</code>","text":"<p><code>diqu</code> is open source software. Whether you are a seasoned open source contributor or a first-time committer, we welcome and encourage you to contribute code, documentation, ideas, or problem statements to this project.</p> <ul> <li>Contributing to <code>diqu</code></li> <li>About this document</li> <li>Getting the code<ul> <li>Installing git</li> <li>External contributors</li> </ul> </li> <li>Setting up an environment<ul> <li>Tools</li> </ul> </li> <li>Testing<ul> <li><code>pytest</code></li> </ul> </li> <li>Submitting a Pull Request</li> </ul>"},{"location":"nav/dev/contributing.html#about-this-document","title":"About this document","text":"<p>There are many ways to contribute to the ongoing development of <code>diqu</code>, such as by participating in discussions and issues.</p> <p>The rest of this document serves as a more granular guide for contributing code changes to <code>diqu</code> (this repository). It is not intended as a guide for using <code>diqu</code>, and some pieces assume a level of familiarity with Python development with <code>poetry</code>. Specific code snippets in this guide assume you are using macOS or Linux and are comfortable with the command line.</p> <ul> <li>Branches: All pull requests from community contributors should target the <code>main</code> branch (default). If the change is needed as a patch for a minor version of dbt that has already been released (or is already a release candidate), a maintainer will backport the changes in your PR to the relevant \"latest\" release branch (<code>1.0.&lt;latest&gt;</code>, <code>1.1.&lt;latest&gt;</code>, ...). If an issue fix applies to a release branch, that fix should be first committed to the development branch and then to the release branch (rarely release-branch fixes may not apply to <code>main</code>).</li> <li>Releases: Before releasing a new minor version, we prepare a series of beta release candidates to allow users to test the new version in live environments. This is an important quality assurance step, as it exposes the new code to a wide variety of complicated deployments and can surface bugs before official release. Releases are accessible via pip.</li> </ul>"},{"location":"nav/dev/contributing.html#getting-the-code","title":"Getting the code","text":""},{"location":"nav/dev/contributing.html#installing-git","title":"Installing git","text":"<p>You will need <code>git</code> in order to download and modify the <code>diqu</code> source code. On macOS, the best way to download git is to just install Xcode.</p>"},{"location":"nav/dev/contributing.html#external-contributors","title":"External contributors","text":"<p>You can contribute to <code>diqu</code> by forking the <code>diqu</code> repository. For a detailed overview on forking, check out the GitHub docs on forking. In short, you will need to:</p> <ol> <li>Fork the <code>diqu</code> repository</li> <li>Clone your fork locally</li> <li>Check out a new branch for your proposed changes</li> <li>Push changes to your fork</li> <li>Open a pull request against <code>infintelambda/diqu</code> from your forked repository</li> </ol>"},{"location":"nav/dev/contributing.html#setting-up-an-environment","title":"Setting up an environment","text":"<p>There are some tools that will be helpful to you in developing locally. While this is the list relevant for <code>diqu</code> development, many of these tools are used commonly across open-source python projects.</p>"},{"location":"nav/dev/contributing.html#tools","title":"Tools","text":"<p>We will buy <code>poetry</code> in <code>diqu</code> development and testing.</p> <p>So first install poetry via pip:</p> <pre><code>python3 -m pip install poetry --upgrade\n</code></pre> <p>then, start installing the local environment:</p> <pre><code>python3 -m poetry install\npython3 -m poetry shell\npoe git-hooks\npip install -e .\ndiqu -h\n</code></pre>"},{"location":"nav/dev/contributing.html#testing","title":"Testing","text":"<p>Once you're able to manually test that your code change is working as expected, it's important to run existing automated tests, as well as adding some new ones. These tests will ensure that:</p> <ul> <li>Your code changes do not unexpectedly break other established functionality</li> <li>Your code changes can handle all known edge cases</li> <li>The functionality you're adding will keep working in the future</li> </ul>"},{"location":"nav/dev/contributing.html#pytest","title":"<code>pytest</code>","text":"<p>Finally, you can also run a specific test or group of tests using <code>pytest</code> directly. With a virtualenv active and dev dependencies installed you can do things like:</p> <pre><code>poe test\n</code></pre> <p>Run test with coverage report:</p> <pre><code>poe test-cov\n</code></pre> <p>See pytest usage docs for an overview of useful command-line options.</p>"},{"location":"nav/dev/contributing.html#submitting-a-pull-request","title":"Submitting a Pull Request","text":"<p>Code can be merged into the current development branch <code>main</code> by opening a pull request. A <code>diqu</code> maintainer will review your PR. They may suggest code revision for style or clarity, or request that you add unit or integration test(s). These are good things! We believe that, with a little bit of help, anyone can contribute high-quality code.</p> <p>Automated tests run via GitHub Actions. If you're a first-time contributor, all tests (including code checks and unit tests) will require a maintainer to approve. Changes in the <code>diqu</code> repository trigger integration tests against Postgres. dbt Labs also provides CI environments in which to test changes to other adapters, triggered by PRs in those adapters' repositories, as well as periodic maintenance checks of each adapter in concert with the latest <code>diqu</code> code changes.</p> <p>Once all tests are passing and your PR has been approved, a <code>diqu</code> maintainer will merge your changes into the active development branch. And that's it! Happy developing </p>"},{"location":"nav/guide/cli.html","title":"CLI Reference","text":""},{"location":"nav/guide/cli.html#cli-reference-diqu","title":"CLI Reference (diqu)","text":"<p>Run <code>diqu --help</code> or <code>diqu -h</code> to see the basic guideline for CLI Reference</p> diqu -h Usage: diqu [OPTIONS] COMMAND [ARGS]...   CLI companion tool to support dq-tools package and more  Options: --version Show the version and exit. --help, -h Show this message and exit.  Commands: alert Alert the incidents   Specify one of these sub-commands and you can find more help from there."},{"location":"nav/guide/cli.html#diqu-alert","title":"diqu alert","text":"<p>Alert the incidents to JIRA Board</p> <p>Examples:</p> CLI (within dbt project)CLI (outside of dbt project) <pre><code>diqu alert\n</code></pre> <pre><code>diqu alert --project-dir /path/to/dbt\n</code></pre>"},{"location":"nav/guide/cli.html#send-alerts-to-other-channels","title":"Send alerts to other channels","text":"Use <code>--to</code> option <pre><code>diqu alert --to &lt;your channel module&gt;\n</code></pre> <p>Current supported channels could be found in <code>(repo)/diqu/alerts/</code>:</p> <ul> <li>JIRA: default</li> <li>Slack: <code>diqu alert --to slack</code></li> </ul>"},{"location":"nav/guide/cli.html#customize-the-alerts-query","title":"Customize the alert's query","text":"Use <code>--query-dir</code> and <code>--query-file</code> option <pre><code>diqu alert \\\n  --query-dir /path/to/dir \\\n  --query-file myquery.sql\n</code></pre> <p>For example, you'd have a query built in <code>myquery.sql</code> file which is located at the root of your dbt project dir e.g. <code>/opt/alert/mydbt/</code>, your command should look like:</p> <pre><code>```bash\ndiqu alert --query-dir /opt/alert/mydbt --query-file myquery.sql\n```\n</code></pre>"},{"location":"nav/guide/cli.html#use-a-specific-dbt-profile-instead-of-pointing-to-the-dbt-project","title":"Use a specific dbt profile instead of pointing to the dbt project","text":"Use <code>--profile-name</code> option <pre><code>diqu alert --profile-name &lt;my_profile&gt;\n</code></pre> <p>For example, the <code>dbt_project.yml</code> is as below:</p> <pre><code>name: 'my_awesome_dbt'\nversion: '1.0.0'\nconfig-version: 2\n\nprofile: 'my_awesome_dbt_profile' # this is the profile name\n...\n</code></pre> <p>And, the <code>profiles.yml</code> content is:</p> <pre><code>my_awesome_dbt_profile:\n    target: snowflake\n    outputs:\n    snowflake:\n        type: snowflake\n        account: \"{{ env_var('DBT_SNOWFLAKE_TEST_ACCOUNT') }}\"\n        user: \"{{ env_var('DBT_SNOWFLAKE_TEST_USER') }}\"\n        password: \"{{ env_var('DBT_ENV_SECRET_SNOWFLAKE_TEST_PASSWORD') }}\"\n        role: \"{{ env_var('DBT_SNOWFLAKE_TEST_ROLE') }}\"\n        database: \"{{ env_var('DBT_SNOWFLAKE_TEST_DATABASE') }}\"\n        warehouse: \"{{ env_var('DBT_SNOWFLAKE_TEST_WAREHOUSE') }}\"\n        schema: \"{{ env_var('DBT_SCHEMA') }}\"\n        threads: 10\n\nmy_other_dbt_profile:\n    target: snowflake\n    ...\n</code></pre> <p>Finally, the command is: <code>diqu alert --profile-name my_awesome_dbt_profile</code> which can be run anywhere (inside or outside of the dbt project dir).</p>"},{"location":"nav/guide/cli.html#configure-the-sql-context-in-case-that-your-tableview-is-on-a-different-schema-or-database-configured-in-the-dbt-profile","title":"Configure the SQL context in case that your table/view is on a different schema or database configured in the dbt profile","text":"Use <code>--query-database</code> and <code>--query-schema</code> option <pre><code>diqu alert --query-database &lt;db&gt; --query-schema &lt;schema&gt;\n</code></pre> <p>Additionally, in the query file dq_tools__get_test_results.sql, you need to have a configuration to specify the main table/view which is:     <pre><code>with\n\nsource as (\n  select * from $database.$schema.dq_issue_log\n),\n...\n</code></pre></p> <ul> <li><code>--query-database</code> value will replace <code>$database</code> placeholder</li> <li><code>--query-schema</code> value will replace <code>$schema</code> placeholder</li> </ul>"},{"location":"nav/guide/config/packages/custom.html","title":"Configuration for Custom query","text":"<p>If you're not using dq-tools package or even not using dbt, no problem, we're supporting a custom query directly to your data table/view.</p> <p>The steps are as following:</p>"},{"location":"nav/guide/config/packages/custom.html#1-prepare-sql-script","title":"1. Prepare SQL script","text":"<p>Assuming we have a custom script named <code>incidents.sql</code> which is located in the current directory.</p> <p>The script need to provide the expected columns required for each channels, for example, for JIRA, we need:</p> <ul> <li>Title</li> <li>Description</li> <li>Label</li> <li>...(to be updated)</li> </ul> <p>Let's build your <code>SELECT</code> query:</p> <pre><code>-- incident.sql\n\nselect  'your_value' as title,\n        ...\n\nfrom    your_table\n</code></pre>"},{"location":"nav/guide/config/packages/custom.html#2-alerting","title":"2. Alerting","text":"<p>See JIRA Configuration for more details, following is a sample command:</p> <pre><code># prepare the env vars here first\n...\n# run alerting\ndiqu alert --query-file incident.sql\n</code></pre>"},{"location":"nav/guide/config/packages/dq-tools.html","title":"Configuration for <code>dq-tools</code> dbt package","text":"<p>This is the essential steps to start alerting the Incidents based on the test results which are captured by  package in a dbt project.</p>"},{"location":"nav/guide/config/packages/dq-tools.html#1-install-dq-tools-package","title":"1. Install <code>dq-tools</code> package","text":"<p>dbt version required: &gt;=1.6.0</p> <p>Include the following in your packages.yml file:</p> <pre><code>packages:\n  - package: infinitelambda/dq_tools\n    version: 1.4.2\n</code></pre> <p>Run <code>dbt deps</code> to install the package.</p> <p>For more information on using packages in your dbt project, check out the dbt Documentation.</p>"},{"location":"nav/guide/config/packages/dq-tools.html#2-configure-the-log-table-the-hook","title":"2. Configure the log table &amp; the hook","text":"<p>Log table is containing all the test results produced by dbt Jobs, and surely can be configured by specifying the database or/and the schema. By default, these info will be getting from the dbt <code>profiles.yml</code>.</p> <p>And the hook is to save the test result if any.</p> <p>In <code>dbt_project.yml</code> file:</p> <pre><code>vars:\n  dbt_dq_tool_schema: AUDIT\n\non-run-end:\n  - '{{ dq_tools.store_test_results(results) }}'\n</code></pre>"},{"location":"nav/guide/config/packages/dq-tools.html#3-build-your-models","title":"3. Build your models","text":"<p>In <code>dq-tools</code>, we decide to save/not to save the test results using the <code>dq_tools_enable_store_test_results</code> variable. By default, it is <code>False</code>, therefore let's enable it to have data flew in.</p> <pre><code># init the dq-tools' models\ndbt run -s dq_tools \n# build your dbt models with saving the test results\ndbt build --vars '{dq_tools_enable_store_test_results: true}'\n</code></pre>"},{"location":"nav/guide/config/packages/dq-tools.html#4-alerting","title":"4. Alerting","text":"<p>See JIRA Configuration for more details, following is a sample command:</p> <pre><code># prepare the env vars here first\n...\n# run alerting\ndiqu alert --query-schema AUDIT\n</code></pre> <p>We need to use <code>--query-schema</code> here because we previously configure the <code>dbt_dq_tool_schema</code> variable</p>"},{"location":"nav/guide/config/sources/custom.html","title":"Configuration for Other connection via CSV file","text":"<p>Currently, the only supported connection is Snowflake, we'll see more added in the near further.</p> <p>In the meantime, using CSV file is a good option alternatively.</p>"},{"location":"nav/guide/config/sources/custom.html#1-configure-the-dbt-profile","title":"1. Configure the dbt profile","text":"<p>Let's create a new target for CSV in dbt <code>profiles.yml</code> file:</p> <pre><code>ci:\n  target: dev\n  outputs:\n    dev:\n      type: csv\n      dir: ./.cache\n      # dir: \"{{ env_var('DQT_CSV_DIR') }}\"\n</code></pre>"},{"location":"nav/guide/config/sources/custom.html#2-generate-csv-file","title":"2. Generate CSV file","text":"<p>No matter what CLI tool you use to query and download data into csv file which located in <code>.cache</code> folder.</p> <p>The default file name is <code>csv__data.csv</code>.</p> <p>And, the file must contain the following columns:</p> <ul> <li>title</li> <li>...(to be updated)</li> </ul>"},{"location":"nav/guide/config/sources/custom.html#3-alerting","title":"3. Alerting","text":"<pre><code>diqu alert --query-dir ./.cache --query_file csv__data.csv --target dev\n</code></pre>"},{"location":"nav/guide/config/sources/snowflake.html","title":"Configuration for Snowflake connection","text":"<p>In order to use Snowflake as the data source, we need to get the additional dependencies after installing <code>diqu</code>:</p> <pre><code>pip install \"snowflake-connector-python[pandas]\"\npip install \"snowflake-connector-python[secure-local-storage]\"\n</code></pre> <p><code>diqu</code> will try to reuse dbt profile configuration with supporting 2 authentication methods:</p>"},{"location":"nav/guide/config/sources/snowflake.html#user-password-authentication","title":"User / Password authentication","text":"<pre><code># ~/.dbt/profiles.yml\nmy-snowflake-db:\n  target: dev\n  outputs:\n    dev:\n      type: snowflake\n      account: [account id]\n\n      # User/password auth\n      user: [username]\n      password: [password]\n\n      role: [user role]\n      database: [database name]\n      warehouse: [warehouse name]\n      schema: [dbt schema]\n</code></pre>"},{"location":"nav/guide/config/sources/snowflake.html#sso-authentication","title":"SSO Authentication","text":"<pre><code># ~/.dbt/profiles.yml\nmy-snowflake-db:\n  target: dev\n  outputs:\n    dev:\n      type: snowflake\n      account: [account id]\n\n      # User\n      user: [username]\n      # SSO config\n      authenticator: externalbrowser\n\n      role: [user role]\n      database: [database name]\n      warehouse: [warehouse name]\n      schema: [dbt schema]\n</code></pre>"}]}