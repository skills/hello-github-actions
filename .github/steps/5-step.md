## Step 5: Merge your workflow and experiment

_Great job! You have created and tested your first GitHub Actions workflow!_ :rocket:

### 📖 Theory: When workflows run

When you created a workflow in a branch, it is only active in that branch until you merge it into the `main` branch. Merging your workflow into `main` makes it available for all future pull requests and changes to your repository.

Once merged, every new pull request you open will automatically trigger the workflow you created.

> [!TIP]
> Unlike the `pull_request` event trigger, some event triggers will only work if the workflow file exists in the `main` branch. For example, workflows that use `workflow_dispatch` (manual runs) or `schedule` (scheduled runs) will not work unless the workflow file is present in `main`.
>
> See [Events that trigger workflows](https://docs.github.com/en/actions/writing-workflows/choosing-when-your-workflow-runs/events-that-trigger-workflows) for more details.

### ⌨️ Activity: Merging your pull request

1. Merge your pull request into the `main` branch.
1. (Optional) Try opening another pull request to see your workflow run again!

