## Step 3: Add a step to your workflow file

_Nice work adding a job to your workflow! :dancer:_

Workflows have jobs, and jobs have steps. So now we'll add a step to your workflow.

**What are _steps_?**: Actions steps run - in the order they are specified, from the top down - when a workflow job is processed. Each step must pass for the next step to run.

Each step consists of either a shell script that's executed, or a reference to an action that's run. When we talk about an action (with a lowercase "a") in this context, we mean a reusable unit of code. You can find out about actions in "[Finding and customizing actions](https://docs.github.com/en/actions/learn-github-actions/finding-and-customizing-actions)," but for now we'll use a shell script in our workflow step.

Update your workflow to make it post a comment on new pull requests. It will do this using a [bash](https://en.wikipedia.org/wiki/Bash_%28Unix_shell%29) script and [GitHub CLI](https://cli.github.com/).

### :keyboard: Activity: Add a step to your workflow file

1. Still working on the `welcome-workflow` branch, open your `welcome.yml` file.
1. Update the contents of the file to:

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
       steps:
         - run: gh pr comment $PR_URL --body "Welcome to the repository!"
           env:
             GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
             PR_URL: ${{ github.event.pull_request.html_url }}
   ```

   **Note:** The step you've added uses GitHub CLI (`gh`) to add a comment when a pull request is opened. To allow GitHub CLI to post a comment, we set the `GITHUB_TOKEN` environment variable to the value of the `GITHUB_TOKEN` secret, which is an installation access token, created when the workflow runs. For more information, see "[Automatic token authentication](https://docs.github.com/en/actions/security-guides/automatic-token-authentication)." We set the `PR_URL` environment variable to the URL of the newly created pull request, and we use this in the `gh` command.
   
1. Click **Commit changes** in the top right of the workflow editor.
1. Type your commit message and commit your changes directly to your branch.
1. Wait about 20 seconds, then refresh this page (the one you're following instructions from). Another workflow will run and will replace the contents of this README file with instructions for the next step.
