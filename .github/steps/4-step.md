## Step 4: Trigger the workflow

_You've now added a fully functioning workflow to your repository! :smile:_

### 📖 Theory: Seeing your workflow in action

All the running and finished workflows can be seen on the **Actions** tab of your repository.

Because you set the workflow to run on the `pull_request` event, it will automatically trigger when a pull request is opened.

> [!TIP]
> Workflow associated to pull request can also be seen on the pull request log near the merge button. You can even [create a rule](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets#require-status-checks-to-pass-before-merging) that prevents merging if the workflow fails! 

### ⌨️ Activity: Trigger the workflow

1. In the **Pull requests** tab, create a pull request from `welcome-workflow` branch into `main`.

1. Notice the comment that the workflow adds to the pull request.

1. Notice the area near the merge button that "All checks have passed".

1. With the pull request created and our workflow triggered, Mona will prepare the next step in this exercise!

### ⌨️ Activity: (optional) Inspect the workflow

1. At the top of the repository, select the **Actions** tab.

1. In the left sidebar, select the workflow named **Post welcome comment**.

  > 💡 **Tip:** You can ignore the other actions. Those were for teaching this exercise.

1. Click the first run entry titled **Welcome workflow** to show a diagram of the run's jobs.

1. Click on the job named **Post welcome comment** to see the full logs.


<details>
<summary>Having trouble? 🤷</summary><br/>

- Check the **Actions** tab for workflow run details and errors.

</details>
