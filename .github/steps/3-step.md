## Step 3: Add a step to your workflow file

_Nice work adding a job to your workflow! :dancer:_

### 📖 Theory: Introduction to steps in jobs

A **step** is an individual task that is part of a job. Steps run in order, top-down, and can be shell scripts or actions. Each step runs in the same environment as the job, and the output of one step can be used by the next.

Steps are the building blocks of jobs, allowing you to automate tasks like checking out code, running commands, or using open source actions from the GitHub Marketplace.

> [!NOTE]
>
> - [Finding and customizing actions](https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/using-pre-written-building-blocks-in-your-workflow)

### ⌨️ Activity: Add a step to your workflow file

1. In the `welcome-workflow` branch, open your `.github/workflows/welcome.yml` file.
1. Add a step to the `welcome` job to post a comment on new pull requests using GitHub CLI:

   ```yaml
   steps:
     - run: gh pr comment "$PR_URL" --body "Welcome to the repository!"
       env:
         GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
         PR_URL: ${{ github.event.pull_request.html_url }}
   ```

1. Commit your changes directly to `welcome-workflow` branch.
1. As you commit your changes Mona will prepare the next step in this exercise!

<details>
<summary>Having trouble? 🤷</summary><br/>

- Make sure the `steps` section is under the `welcome` job and properly indented.
- Ensure you have the correct environment variables set.

</details>
