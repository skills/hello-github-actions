## Step 2: Add a job to your workflow file

Nice work! :tada: You added a workflow file!

### 📖 Theory: Introduction to jobs

A [job](https://docs.github.com/en/actions/about-github-actions/understanding-github-actions#jobs) is a group of steps that run together on the same [runner](https://docs.github.com/en/actions/using-github-hosted-runners/using-github-hosted-runners/about-github-hosted-runners) within a workflow. Each job is defined under the `jobs` section and runs independently and in parallel by default.

Jobs help you organize your workflow into logical units, such as building, testing, or deploying your code.

> [!Tip]
> You can define a job to run with multiple [variations using a matrix strategy](https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/running-variations-of-jobs-in-a-workflow).

### ⌨️ Activity: Add a job to your workflow file

1. In the `welcome-workflow` branch, open your `.github/workflows/welcome.yml` file.

1. Edit the file to add the `jobs` section and 1 job named `welcome`, which will run on the latest Ubuntu operating system.

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

1. Commit your changes to the `welcome-workflow` branch.

1. With the job information added, Mona will review your work and prepare the next step in this exercise!

<details>
<summary>Having trouble? 🤷</summary><br/>

- Make sure the `jobs` section is properly indented in your YAML file.
- Confirm you are editing the correct file and branch.

</details>
