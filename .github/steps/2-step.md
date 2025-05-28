## Step 2: Add a job to your workflow file

Nice work! :tada: You added a workflow file!

### 📖 Theory: What is a job in GitHub Actions?

> [!NOTE]
> A job is a set of steps in a workflow that execute on the same runner. Workflows have jobs, and jobs have steps. Steps are executed in order and are dependent on each other.

- [Jobs in GitHub Actions](https://docs.github.com/en/actions/learn-github-actions/understanding-github-actions#jobs)

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
     build:
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
