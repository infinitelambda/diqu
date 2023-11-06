var __index = {"config":{"lang":["en"],"separator":"[\\s\\-,:!=\\[\\]()\"`/]+|\\.(?!\\d)|&[lg]t;|(?!\\b)(?=[A-Z][a-z])","pipeline":["stopWordFilter"]},"docs":[{"location":"index.html","title":"diqu","text":"<p>CLI companion tool supporting the Alert / Notification for  and more.</p>"},{"location":"index.html#installation","title":"Installation","text":"pip install diqu --upgrade Successfully installed diqu restart \u21bb <p>\ud83d\udcd3 NOTE: The DWH module should get installed already if you use <code>diqu</code> in a dbt project, if not, please perform additional step, for example, to install snowflake module:</p> <pre><code>pip install \"snowflake-connector-python[pandas]\"\npip install \"snowflake-connector-python[secure-local-storage]\"\n</code></pre>"},{"location":"index.html#usage","title":"Usage","text":"<pre><code>dbt run -s dq_tools\ndiqu alert \\\n  --project-dir /path/to/dbt/project \\\n  --to slack --to jira\n</code></pre> Sample logs <pre><code>04:33:17  diqu: INFO - Run with diqu==1.0.0 \ud83c\udfc3\n04:33:19  diqu: INFO - Using dbt project at: /path/to/dbt/project\n04:33:19  diqu: INFO - Using dbt profiles.yml at: ~/.dbt\n04:33:19  diqu: INFO - Using snowflake connection\n04:33:19  diqu: INFO - Looking for the query in: /path/to/site-packages/diqu/packages/include/dq_tools__get_test_results.sql\n04:33:23  diqu: INFO - Alerting to channel: SLACK\n04:33:23  diqu: INFO - \u2705 Done &gt; Slack\n04:33:23  diqu: INFO - Alerting to channel: JIRA\n04:33:23  diqu: INFO - \u2705 Done &gt; JIRA\n</code></pre> <p>In particular to the alert module, here are the additional configurations:</p> <ul> <li>For SLACK, you need to use the environment variables to configure the Slack Channel:</li> </ul> <pre><code>export SLACK_TOKEN=your_token\nexport SLACK_CHANNEL=your_channel_name\ndiqu alert --to slack\n</code></pre> <ul> <li>For JIRA, you need to use the environment variables to configure the JIRA Board:</li> </ul> <pre><code>export JIRA_SERVER=your_jira_server e.g. https://your_value.atlassian.net/\nexport JIRA_AUTH_USER=your_service_account e.g. dqt_user@your_value.com\nexport JIRA_AUTH_PASSWORD=your_service_token e.g. ATATTxxxxx\nexport JIRA_PROJECT_ID=your_project_id e.g. 106413\nexport JIRA_INCIDENT_TICKET_TYPE=your_ticket_type, default to \"[System] Incident\"\nexport JIRA_OPEN_TICKETS_FILTER=your_ticket_filter_on_title, default to \"*dq_tools\"\ndiqu alert --to jira\n</code></pre>"},{"location":"index.html#how-to-contribute","title":"How to Contribute","text":"<p>See CONTRIBUTING.md</p>"},{"location":"index.html#about-infinite-lambda","title":"About Infinite Lambda","text":"<p>Infinite Lambda is a cloud and data consultancy. We build strategies, help organisations implement them and pass on the expertise to look after the infrastructure.</p> <p>We are an Elite Snowflake Partner, a Platinum dbt Partner and two-times Fivetran Innovation Partner of the Year for EMEA.</p> <p>Naturally, we love exploring innovative solutions and sharing knowledge, so go ahead and:</p> <p>\ud83d\udd27 Take a look around our Git  \u270f\ufe0f Browse our tech blog</p> <p>We are also chatty, so:</p>"},{"location":"index.html#follow-us-on-linkedin","title":"\ufe0f\u20e3 Follow us on LinkedIn","text":"<p>\ud83d\udc4b\ud83c\udffc Or just get in touch</p> <p></p>"},{"location":"nav/dev/changelog.html","title":"TBU","text":""},{"location":"nav/dev/contributing.html","title":"Contributing to <code>diqu</code>","text":"<p><code>diqu</code> is open source software. Whether you are a seasoned open source contributor or a first-time committer, we welcome and encourage you to contribute code, documentation, ideas, or problem statements to this project.</p> <ul> <li>Contributing to <code>diqu</code></li> <li>About this document</li> <li>Getting the code<ul> <li>Installing git</li> <li>External contributors</li> </ul> </li> <li>Setting up an environment<ul> <li>Tools</li> </ul> </li> <li>Testing<ul> <li><code>pytest</code></li> </ul> </li> <li>Submitting a Pull Request</li> </ul>"},{"location":"nav/dev/contributing.html#about-this-document","title":"About this document","text":"<p>There are many ways to contribute to the ongoing development of <code>diqu</code>, such as by participating in discussions and issues.</p> <p>The rest of this document serves as a more granular guide for contributing code changes to <code>diqu</code> (this repository). It is not intended as a guide for using <code>diqu</code>, and some pieces assume a level of familiarity with Python development with <code>poetry</code>. Specific code snippets in this guide assume you are using macOS or Linux and are comfortable with the command line.</p> <ul> <li>Branches: All pull requests from community contributors should target the <code>main</code> branch (default). If the change is needed as a patch for a minor version of dbt that has already been released (or is already a release candidate), a maintainer will backport the changes in your PR to the relevant \"latest\" release branch (<code>1.0.&lt;latest&gt;</code>, <code>1.1.&lt;latest&gt;</code>, ...). If an issue fix applies to a release branch, that fix should be first committed to the development branch and then to the release branch (rarely release-branch fixes may not apply to <code>main</code>).</li> <li>Releases: Before releasing a new minor version, we prepare a series of beta release candidates to allow users to test the new version in live environments. This is an important quality assurance step, as it exposes the new code to a wide variety of complicated deployments and can surface bugs before official release. Releases are accessible via pip.</li> </ul>"},{"location":"nav/dev/contributing.html#getting-the-code","title":"Getting the code","text":""},{"location":"nav/dev/contributing.html#installing-git","title":"Installing git","text":"<p>You will need <code>git</code> in order to download and modify the <code>diqu</code> source code. On macOS, the best way to download git is to just install Xcode.</p>"},{"location":"nav/dev/contributing.html#external-contributors","title":"External contributors","text":"<p>You can contribute to <code>diqu</code> by forking the <code>diqu</code> repository. For a detailed overview on forking, check out the GitHub docs on forking. In short, you will need to:</p> <ol> <li>Fork the <code>diqu</code> repository</li> <li>Clone your fork locally</li> <li>Check out a new branch for your proposed changes</li> <li>Push changes to your fork</li> <li>Open a pull request against <code>infintelambda/diqu</code> from your forked repository</li> </ol>"},{"location":"nav/dev/contributing.html#setting-up-an-environment","title":"Setting up an environment","text":"<p>There are some tools that will be helpful to you in developing locally. While this is the list relevant for <code>diqu</code> development, many of these tools are used commonly across open-source python projects.</p>"},{"location":"nav/dev/contributing.html#tools","title":"Tools","text":"<p>We will buy <code>poetry</code> in <code>diqu</code> development and testing.</p> <p>So first install poetry via pip:</p> <pre><code>python3 -m pip install poetry --upgrade\n</code></pre> <p>then, start installing the local environment:</p> <pre><code>python3 -m poetry install\npython3 -m poetry shell\npoe git-hooks\npip install -e .\ndiqu -h\n</code></pre>"},{"location":"nav/dev/contributing.html#testing","title":"Testing","text":"<p>Once you're able to manually test that your code change is working as expected, it's important to run existing automated tests, as well as adding some new ones. These tests will ensure that:</p> <ul> <li>Your code changes do not unexpectedly break other established functionality</li> <li>Your code changes can handle all known edge cases</li> <li>The functionality you're adding will keep working in the future</li> </ul>"},{"location":"nav/dev/contributing.html#pytest","title":"<code>pytest</code>","text":"<p>Finally, you can also run a specific test or group of tests using <code>pytest</code> directly. With a virtualenv active and dev dependencies installed you can do things like:</p> <pre><code>poe test\n</code></pre> <p>Run test with coverage report:</p> <pre><code>poe test-cov\n</code></pre> <p>See pytest usage docs for an overview of useful command-line options.</p>"},{"location":"nav/dev/contributing.html#submitting-a-pull-request","title":"Submitting a Pull Request","text":"<p>Code can be merged into the current development branch <code>main</code> by opening a pull request. A <code>diqu</code> maintainer will review your PR. They may suggest code revision for style or clarity, or request that you add unit or integration test(s). These are good things! We believe that, with a little bit of help, anyone can contribute high-quality code.</p> <p>Automated tests run via GitHub Actions. If you're a first-time contributor, all tests (including code checks and unit tests) will require a maintainer to approve. Changes in the <code>diqu</code> repository trigger integration tests against Postgres. dbt Labs also provides CI environments in which to test changes to other adapters, triggered by PRs in those adapters' repositories, as well as periodic maintenance checks of each adapter in concert with the latest <code>diqu</code> code changes.</p> <p>Once all tests are passing and your PR has been approved, a <code>diqu</code> maintainer will merge your changes into the active development branch. And that's it! Happy developing </p>"},{"location":"nav/guide/cli.html","title":"CLI Reference","text":""}]}