## Step 2: Add a job to your workflow file

Nice work! :tada: You added a workflow file!

### 📖 Theory: Introduction to jobs in GitHub Actions workflows

A **job** is a group of steps that run together on the same runner within a workflow. Jobs are defined in the workflow file under the `jobs` section. Each job runs independently by default, but you can configure jobs to depend on each other.

Jobs help you organize your workflow into logical units, such as building, testing, or deploying your code. Each job can run on different environments and can be configured to run in parallel or sequentially.

> [!NOTE]
>
> - [Jobs in GitHub Actions](https://docs.github.com/en/actions/learn-github-actions/understanding-github-actions#jobs)

### ⌨️ Activity: Add a job to your workflow file

1. In the `welcome-workflow` branch, open your `.github/workflows/welcome.yml` file.
1. Edit the file to add a job section as shown below:

   ```yaml
   name: Post welcome comment
   on:
     pull_request:
       types: [opened]
   permissions:
     pull-requests: write
   jobs:
     welcome:
       name: Post welcome comment
       runs-on: ubuntu-latest
   ```

1. Commit your changes directly to the `welcome-workflow` branch.
1. As you commit your changes Mona will prepare the next step in this exercise!

<details>
<summary>Having trouble? 🤷</summary><br/>

- Make sure the `jobs` section is properly indented in your YAML file.
- Confirm you are editing the correct file and branch.

</details>
