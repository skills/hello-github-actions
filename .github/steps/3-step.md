## Step 3: Add a step to your workflow file

_Nice work adding a job to your workflow! :dancer:_

### 📖 Theory: What are steps in a workflow?

> [!NOTE]
> Steps run in order, top-down, when a workflow job is processed. Each step must pass for the next to run. Each step is either a shell script or a reference to an action.

- [Finding and customizing actions](https://docs.github.com/en/actions/learn-github-actions/finding-and-customizing-actions)

### ⌨️ Activity: Add a step to your workflow file

1. In the `welcome-workflow` branch, open your `.github/workflows/welcome.yml` file.
1. Add a step to the `build` job to post a comment on new pull requests using GitHub CLI:

   ```yaml
   steps:
     - run: gh pr comment $PR_URL --body "Welcome to the repository!"
       env:
         GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
         PR_URL: ${{ github.event.pull_request.html_url }}
   ```

1. Commit your changes directly to your branch.
1. Wait about 20 seconds, then refresh this page.

<details>
<summary>Having trouble? 🤷</summary><br/>

- Make sure the `steps` section is under the `build` job and properly indented.
- Ensure you have the correct environment variables set.

</details>
