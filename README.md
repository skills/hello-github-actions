<!--
  <<< Author notes: Header of the course >>>
  Include a 1280x640 image, course title in sentence case, and a concise description in emphasis.
  In your repository settings: enable template repository, add your 1280x640 social image, auto delete head branches.
  Add your open source license, GitHub uses Creative Commons Attribution 4.0 International.
-->

<img src=https://user-images.githubusercontent.com/1221423/156946922-c6167732-6171-4233-899b-5a6216e1a363.svg width=300 align=right>

# Hello GitHub Actions

_Create a GitHub Action and use it in a workflow._

<!--
  <<< Author notes: Start of the course >>>
  Include start button, a note about Actions minutes,
  and tell the learner why they should take the course.
  Each step should be wrapped in <details>/<summary>, with an `id` set.
  The start <details> should have `open` as well.
  Do not use quotes on the <details> tag attributes.
-->

<details id=0 open>
<summary><h2>:golf: Start</h2></summary>

[![start-course](https://user-images.githubusercontent.com/1221423/154366775-5491926f-9ed1-4a4a-a229-0810c0ed7e5e.svg)](https://github.com/githublearn/hello-github-actions/generate)

> When you select **Start course** or **Use this template**, you will be prompted to create a new repository.
> We recommend creating a public repository, as private repositories will [use Actions minutes](https://docs.github.com/billing/managing-billing-for-github-actions/about-billing-for-github-actions).<br>
> After you make your own repository, wait about 20 seconds and refresh. I will go to the next step.

Automation is key for streamlining your work processes, and [GitHub Actions](https://docs.github.com/actions) is the best way to supercharge your workflow.

- **Who is this for**: Developers, DevOps engineers, students, managers, teams, GitHub users.
- **What you'll learn**: Create workflow files, trigger workflows, find workflow logs.
- **What you'll build**: An Actions workflow that will check emoji shortcode references in Markdown files.
- **Prerequisites**: In this course you will work with issues and pull requests, as well as edit files. We recommend you take the [Introduction to GitHub](/githublearn/introduction-to-github) course first!
- **How long**: This course is five steps long and can be finished in less than two hours to complete.

</details>

<!--
  <<< Author notes: Step 1 >>>
  Choose 3-5 steps for your course.
  The first step is always the hardest, so pick something easy!
  Link to docs.github.com for further explanations.
  Encourage users to open new tabs for steps!
-->

<details id=1>
<summary><h2>:pencil: Step 1: Create a workflow file</h2></summary>

_Welcome to "Hello GitHub Actions"! :wave:_

**What is _GitHub Actions_**: Actions are a flexible way to automate nearly every aspect of your team's software workflow. You can automate testing, continuously deploy, review code, manage issues and pull requests, and much more. The best part, these workflows are stored as code in your repository and easily shared and reused across teams. To learn more, check out the [GitHub Actions feature page](https://github.com/features/actions), or the [GitHub Actions documentation](https://docs.github.com/actions).

First, we'll define a **workflow** that uses the action.

**What is a _workflow_**: Workflows are defined in special files in the `.github/workflows` directory. Workflows can execute based on your chosen event. For this lab, we'll be using the [`push`](https://docs.github.com/en/developers/webhooks-and-events/webhooks/webhook-events-and-payloads#push) event.

We went ahead and made a branch and pull request for you.

### :keyboard: Activity: Create a workflow file

1. Open a new browser tab, and work on the steps in your second tab while you read the instructions in this tab.
1. Open the pull request from the `emoji-workflow` branch.
1. Add a file at `.github/workflows/emoji.yml` on the `emoji-workflow` branch.
1. Add the following content to the `emoji.yml` file:
   ```yaml
   name: Check emoji shortcode
   on: push
   ```
1. Commit the changes.
1. Wait about 20 seconds then refresh this page for the next step.

</details>

<!--
  <<< Author notes: Step 2 >>>
  Start this step by acknowledging the previous step.
  Define terms and link to docs.github.com.
  Historic note: The previous course had troubleshooting steps for people not using the GitHub UI.
-->

<details id=2>
<summary><h2>:beginner: Step 2: Add a job to your workflow file</h2></summary>

_Nice work! :tada: You added a workflow!_

Here's what it means:

- `name: A workflow for my Hello World file` gives your workflow a name. This name appears on any pull request or in the Actions tab.
- `on: push` indicates that your workflow will execute anytime code is pushed to your repository.

Next, we need to specify jobs to run.

**What is a _job_**: Workflows have jobs, and jobs have steps.

In this step, we will add a "build" job. We will specify `ubuntu-latest` as the fastest and cheapest job runner available.

### :keyboard: Activity: Add a job to your workflow file

1. Update `emoji.yml` in the `emoji-workflow` branch to:
   ```yaml
   name: Check emoji shortcode
   on: push
   jobs:
     build:
       name: Check emoji shortcode
       runs-on: ubuntu-latest
   ```
1. Click **Start commit** in the top right of the workflow editor.
1. Type your commit message and commit your changes directly to your branch.
1. Wait about 20 seconds then refresh this page for the next step.

</details>

<!--
  <<< Author notes: Step 3 >>>
  Start this step by acknowledging the previous step.
  Define terms and link to docs.github.com.
-->

<details id=3>
<summary><h2>:mechanical_arm: Step 3: Add actions to your workflow file</h2></summary>

_Nice work adding a job to your workflow! :dancer:_

Workflows have jobs, and jobs have steps. So now we'll add steps.

**What are _steps_**: Action steps will run during our job in order. Each step must pass for the next step to run. Action steps can be used from within the same repository, from any other public repository, or from a published Docker container image.

In our action,
1. We will `git checkout` the code, using a [pre-built checkout action](https://github.com/actions/checkout).
2. We'll run a [bash](https://en.wikipedia.org/wiki/Bash_%28Unix_shell%29) script to check Markdown files.
3. We'll fail (`exit 1`) if any Markdown file contains an emoji without using [emoji shortcodes](https://github.com/ikatyang/emoji-cheat-sheet/blob/master/README.md).

### :keyboard: Activity: Add actions to your workflow file

1. Update `emoji.yml` in the `emoji-workflow` branch to:
   ```yaml
   name: Check emoji shortcode
   on: push
   jobs:
     build:
       name: Check emoji shortcode
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v2
         - run: |
             if LC_ALL=C grep -R '[^ -~]' *.md; then
               echo "Use emoji shortcodes instead!"
               echo "See https://github.com/ikatyang/emoji-cheat-sheet/blob/master/README.md"
               exit 1
             fi
   ```
1. Click **Start commit** in the top right of the workflow editor.
1. Type your commit message and commit your changes directly to your branch.
1. Wait about 20 seconds then refresh this page for the next step.

</details>

<!--
  <<< Author notes: Step 4 >>>
  Start this step by acknowledging the previous step.
  Define terms and link to docs.github.com.
-->

<details id=4>
<summary><h2>:chipmunk: Step 4: Merge your workflow file</h2></summary>

_You're now able to write and run Actions workflows! :heart:_

Merge this pull request so the action will be a part of the `main` branch.

### :keyboard: Activity: Merge your workflow file

1. Merge the pull request from branch `emoji-workflow`.
1. Delete your `emoji-workflow` branch (optional).
1. Wait about 20 seconds then refresh this page for the next step.

</details>

<!--
  <<< Author notes: Step 5 >>>
  Start this step by acknowledging the previous step.
  Define terms and link to docs.github.com.
-->

<details id=5>
<summary><h2>:arrow_forward: Step 5: Trigger the workflow</h2></summary>

_You've now got a fully functioning workflow! :smile:_

This action will run any time a new commit is created or pushed to the remote repository. Since you just created a commit, the workflow should have been triggered.

**Seeing your _action_ in action**: The status of your action is shown here in the pull request (look for **All checks have passed** below), or you can click the "Actions" tab in your repository. From there you will see the actions that have run, and you can click on the action's "Log" link to view details.

![View an action's log](https://user-images.githubusercontent.com/16547949/62388049-4e64e600-b52a-11e9-8bf5-db0c5452360f.png)

### :keyboard: Activity: Trigger the workflow

1. Make a new branch: `test-workflow`.
1. Commit any change to your branch, such as adding an emoji to your README.md file.
1. Open a pull request with branch: `test-workflow`.
1. See your action run on your pull request.
1. Wait about 20 seconds then refresh this page for the next step.

</details>

<!--
  <<< Author notes: Finish >>>
  Review what we learned, ask for feedback, provide next steps.
-->

<details id=X>
<summary><h2>:checkered_flag: Finish</h2></summary>

_Congratulations friend, you've completed this course!_

<img src=https://octodex.github.com/images/jetpacktocat.png alt=celebrate width=300 align=right>

Here's a recap of all the tasks you've accomplished in your repository:

- You've created your first GitHub Actions workflow.
- You learned where to make your workflow file.
- You created an event trigger, a job, and steps for your workflow.
- You're ready to automate anything you can dream of.

### What's next?

- Review the [GitHub Actions documentation](https://docs.github.com/actions/learn-github-actions) on GitHub Docs.
- Use actions created by others in [awesome-actions](https://github.com/sdras/awesome-actions).
- We'd love to hear what you thought of this course [in our community forum](https://github.community/c/education/github-learning-lab/34).
- [Take another GitHub Learn course](https://github.com/githublearn).
- [Read the GitHub Getting Started docs](https://docs.github.com/get-started).
- To find projects to contribute to, check out [GitHub Explore](https://github.com/explore).

</details>

<!--
  <<< Author notes: Footer >>>
  Add a link to get support, GitHub status page, code of conduct, license link.
-->

---

Get help: [Post in our community forum](https://github.community/c/education/github-learning-lab/34) &bull; [Review the GitHub status page](https://www.githubstatus.com/)

&copy; 2022 GitHub &bull; [Code of Conduct](https://www.contributor-covenant.org/version/2/1/code_of_conduct/code_of_conduct.md) &bull; [CC-BY-4.0 License](https://creativecommons.org/licenses/by/4.0/legalcode)
