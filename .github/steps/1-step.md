## Step 1: Create a workflow file

Welcome to "Hello GitHub Actions" exercise! :wave:

### 📖 Theory: What is GitHub Actions and a workflow?

> [!NOTE]
> GitHub Actions is a flexible way to automate nearly every aspect of your team's software workflow. Workflows are defined in special files in the `.github/workflows` directory and execute based on your chosen event.

- [GitHub Actions feature page](https://github.com/features/actions)
- [GitHub Actions documentation](https://docs.github.com/actions)
- [Understanding GitHub Actions](https://docs.github.com/en/actions/learn-github-actions/understanding-github-actions)
- [pull_request event](https://docs.github.com/en/developers/webhooks-and-events/webhooks/webhook-events-and-payloads#pull_request)

### ⌨️ Activity: Create a workflow file and open a pull request

1. Open this repository in a new browser tab so you can work on the steps while you read the instructions in this tab.
1. Create a new branch named `welcome-workflow`.
1. In the `welcome-workflow` branch, create a new file at `.github/workflows/welcome.yml` with the following content:

   ```yaml
   name: Post welcome comment
   on:
     pull_request:
       types: [opened]
   permissions:
     pull-requests: write
   ```

1. Commit your changes directly to the `welcome-workflow` branch.
1. Create a pull request from the `welcome-workflow` branch to `main`.
1. Wait about 20 seconds, then refresh this page.

<details>
<summary>Having trouble? 🤷</summary><br/>

- Make sure you are on the `welcome-workflow` branch when creating the workflow file.
- Double-check the file path and YAML indentation.

</details>
