## Step 1: Create a workflow file

Welcome to "Hello GitHub Actions" exercise! :wave:

### 📖 Theory: Introduction to workflows

A **workflow** is an automated process that you define in your repository. Workflows are described in YAML files stored in the `.github/workflows` directory. Each workflow is triggered by specific **events**—such as opening a pull request, pushing code, or creating an issue—that happen in your repository.

Workflows let you automate tasks like building, testing, or deploying your code, and can respond to almost any activity in your project.

> [!NOTE]
> If you want to learn more check out these resources:
> - [Understanding GitHub Actions](https://docs.github.com/en/actions/learn-github-actions/understanding-github-actions)
> - [Events that trigger workflows](https://docs.github.com/en/actions/writing-workflows/choosing-when-your-workflow-runs/events-that-trigger-workflows#pull_request)

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

1. Commit your changes directly to the `welcome-workflow` branch.
1. As you commit your changes Mona will prepare the next step in this exercise!

<details>
<summary>Having trouble? 🤷</summary><br/>

- Make sure you are on the `welcome-workflow` branch when creating the workflow file.
- Double-check the file path and YAML indentation.

</details>
