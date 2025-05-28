## Step 5: Merge and experiment

_Great job! You have created and tested your first GitHub Actions workflow!_ :rocket:

### 📖 Theory: When workflows run

When you create a workflow in a branch, it is only enabled for that branch until you merge it into the default branch (`main`). When a workflow is in the default branch it applies to the entire repository.

Every new pull request regardless of branch will now automatically trigger the workflow you created.

> [!TIP]
> Some event triggers, like [workflow_dispatch](https://docs.github.com/en/actions/writing-workflows/choosing-when-your-workflow-runs/events-that-trigger-workflows#workflow_dispatch) and [schedule](https://docs.github.com/en/actions/writing-workflows/choosing-when-your-workflow-runs/events-that-trigger-workflows#schedule) will only work if the workflow file exists in default branch. 

### ⌨️ Activity: Merging your pull request

1. Merge your pull request into the `main` branch.

1. (Optional) Try opening another pull request to see your workflow run again!

