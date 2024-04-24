## Step 2: Add a job to your workflow file

_Nice work! :tada: You added a workflow file!_

Here's what the entries in the `welcome.yml` file, on the `welcome-workflow` branch, mean:

- `name: Post welcome comment` gives your workflow a name. This name will appear in the Actions tab of your repository.
- `on: pull_request: types: [opened]` indicates that your workflow will execute whenever someone opens a pull request in your repository.
- `permissions` assigns the workflow permissions to operate on the repository
- `pull-requests: write` gives the workflow permission to write to pull requests. This is needed to create the welcome comment.

Next, we need to specify jobs to run.

**What is a _job_?**: A job is a set of steps in a workflow that execute on the same runner (a runner is a server that runs your workflows when triggered). Workflows have jobs, and jobs have steps. Steps are executed in order and are dependent on each other. You'll add steps to your workflow later in the course. To read more about jobs, see "[Jobs](https://docs.github.com/en/actions/learn-github-actions/understanding-github-actions#jobs)".

In the following activity, you'll add a "build" job to your workflow. You'll specify `ubuntu-latest` as the fastest, and cheapest, job runner available. If you want to read more about why we'll use that runner, see the code explanation for the line `runs-on: ubuntu-latest` in the "[Understanding the workflow file](https://docs.github.com/en/actions/learn-github-actions/understanding-github-actions#understanding-the-workflow-file)" article.

### :keyboard: Activity: Add a job to your workflow file

1. In a separate browser tab, make sure you are on the `welcome-workflow` branch and open your `.github/workflows/welcome.yml` file.
1. Edit the file and update its contents to:

   ```yaml copy
   name: Post welcome comment
   on:
     pull_request:
       types: [opened]
   permissions:
     pull-requests: write
   jobs:
     build:
       name: Post welcome comment
       runs-on: ubuntu-latest
   ```

1. Click **Commit changes** in the top right of the workflow editor.
1. Type a commit message and commit your changes directly to the `welcome-workflow` branch.
1. Wait about 20 seconds, then refresh this page (the one you're following instructions from). Another workflow will run and will replace the contents of this README file with instructions for the next step.
