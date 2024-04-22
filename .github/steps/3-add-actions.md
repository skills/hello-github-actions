## Step 3: Add a step to your workflow file

_Nice work adding a job to your workflow! :dancer:_

Workflows have jobs, and jobs have steps. So now we'll add a step to your workflow.

**What are _steps_?**: Actions steps run - in the order they are specified, from the top down - when a workflow job is processed. Each step is either a shell script that's executed, or an action that's run. Each step must pass for the next step to run. Actions steps can be used from within the same repository, from any other public repository, or from a published Docker container image.

In our action, we post a comment on the pull request using a [bash](https://en.wikipedia.org/wiki/Bash_%28Unix_shell%29) script and [GitHub CLI](https://cli.github.com/).

### :keyboard: Activity: Add a step to your workflow file

1. Open your `welcome.yml` file.
1. Update the contents of the file to:
   ```yaml
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
1. Click **Commit changes...** in the top right of the workflow editor.
1. Type your commit message and commit your changes directly to your branch.
1. Wait about 20 seconds, then refresh this page (the one you're following instructions from). Another workflow will run and will replace this content with instructions for the next step.
