## Step 4: Trigger the workflow

_You've now added a fully functioning workflow to your repository! :smile:_

### 📖 Theory: Seeing your workflow in action

Because you set the workflow to run on the `pull_request` event, it will automatically trigger when a pull request is opened.

> [!NOTE]
> The status of each workflow run that's triggered is shown in the pull request before it's merged. You can also see a list of all the workflows that are running, or have finished running, in the **Actions** tab of your repository.

### ⌨️ Activity: Trigger the workflow

1. In the **Pull requests** tab, create a pull request from `welcome-workflow` branch into `main`.
1. Notice the comment that the workflow adds to the pull request.


<details>
<summary>Having trouble? 🤷</summary><br/>

- Check the **Actions** tab for workflow run details and errors.

</details>
