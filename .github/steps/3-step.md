## Step 3: Add a step to your workflow file

_Nice work adding a job to your workflow! :dancer:_

### 📖 Theory: Introduction to steps in jobs

[Steps](https://docs.github.com/en/actions/writing-workflows/workflow-syntax-for-github-actions#jobsjob_idsteps) are the building blocks of jobs, allowing you to automate tasks like checking out code, running commands, or using open source Actions. They run sequentially in the job's environment but as independent processes. Unlike traditional code with a shared variable space, [inputs](https://docs.github.com/en/actions/sharing-automations/creating-actions/metadata-syntax-for-github-actions#inputs) and [outputs](https://docs.github.com/en/actions/sharing-automations/creating-actions/metadata-syntax-for-github-actions#outputs-for-docker-container-and-javascript-actions) must be explicitly declared.

> [!TIP]
> The best part of GitHub Actions is the [marketplace](https://github.com/marketplace?type=actions) where the community has already built many free useful tools to [find and customize](https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/using-pre-written-building-blocks-in-your-workflow)!

### ⌨️ Activity: Add a step to your workflow file

1. In the `welcome-workflow` branch, open your `.github/workflows/welcome.yml` file.

1. Add a step to the `welcome` job to post a comment on new pull requests using GitHub CLI:

   ```yaml
   name: Post welcome comment
   on:
     pull_request:
       types: [opened]
   permissions:
     pull-requests: write
   jobs:
     welcome:
       name: Post welcome comment
       runs-on: ubuntu-latest
       steps:
         - run: gh pr comment "$PR_URL" --body "Welcome to the repository!"
           env:
             GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
             PR_URL: ${{ github.event.pull_request.html_url }}
   ```

1. Commit your changes directly to `welcome-workflow` branch.

1. With the step information added, Mona will review your work and prepare the next step in this exercise!

<details>
<summary>Having trouble? 🤷</summary><br/>

- Make sure the `steps` section is under the `welcome` job and properly indented.
- Ensure you have the correct environment variables set.

</details>
