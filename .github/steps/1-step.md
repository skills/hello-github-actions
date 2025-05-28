## Step 1: Create a workflow file

### 📖 Theory: Introduction to workflows

A **workflow** is an automated process that you define in your repository. Workflows are described in YAML files stored in the `.github/workflows` directory. Each workflow is triggered by specific [events](https://docs.github.com/en/actions/writing-workflows/choosing-when-your-workflow-runs/events-that-trigger-workflows) happening in your repository such as opening a pull request, pushing code, or creating an issue.

Workflows let you automate tasks like building, testing, or deploying your code, and can respond to almost any activity in your project.

> [!NOTE]
> If you want to learn more check out these resources:
> - [Understanding GitHub Actions](https://docs.github.com/en/actions/learn-github-actions/understanding-github-actions)
> - [Events that trigger workflows](https://docs.github.com/en/actions/writing-workflows/choosing-when-your-workflow-runs/events-that-trigger-workflows)

### ⌨️ Activity: Create a workflow file

1. Open this repository in a new browser tab so you can work on the steps while you read the instructions in this tab.

1. In the **Code** tab of your repository, create a new branch named `welcome-workflow`.

   <img width="400" alt="create branch screenshot" src="https://github.com/user-attachments/assets/8aa4a918-c877-4214-9efe-c9a99ca6421b" />

1. In the `welcome-workflow` branch, navigate to the `.github/workflows` directory.

1. Create a new file named `welcome.yml` in the `.github/workflows` directory with the following content:

   ```yaml
   name: Post welcome comment
   on:
     pull_request:
       types: [opened]
   permissions:
     pull-requests: write
   ```

   > [!NOTE]
   > This is an incomplete workflow file. It is normal if you receive an error message. One step at a time! 😎

1. Commit your changes directly to the `welcome-workflow` branch.

1. With your workflow file committed, Mona will check your work and prepare the next step in this exercise!

<details>
<summary>Having trouble? 🤷</summary><br/>

- Make sure you are on the `welcome-workflow` branch when creating the workflow file.
- Double-check the file path and YAML indentation.

</details>
