## Step 4: Trigger the workflow

_You've now added a fully functioning workflow to your repository! :smile:_

The shell script in the workflow will run whenever a new pull request is opened.

### 📖 Theory: Seeing your action in action

> [!NOTE]
> The status of each workflow run that's triggered is shown in the pull request before it's merged. You can also see a list of all the workflows that are running, or have finished running, in the **Actions** tab of your repository.

### ⌨️ Activity: Trigger the workflow

1. In the **Pull requests** tab, create a pull request that will merge `welcome-workflow` into `main`.
1. Watch the workflow running in the checks section of the pull request.
1. Notice the comment that the workflow adds to the pull request.


<details>
<summary>Having trouble? 🤷</summary><br/>

- Make sure your workflow file is in the correct location and named properly.
- Check the **Actions** tab for workflow run details and errors.

</details>
