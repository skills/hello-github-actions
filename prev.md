# GitHub Actions: Hello World

_Create a GitHub Action and use it in a workflow._

![](https://repository-images.githubusercontent.com/200244092/c64f8080-586d-11ea-9f2b-fc72525069dd)

**Tags**: GitHub Actions, Workflows, Hello World

---

Automation is key for streamlining your work processes, and GitHub Actions are the best way to supercharge your workflow.

## What you'll learn

- Organize and identify workflow files
- Add executable scripts
- Create workflow and action blocks
- Trigger workflows
- Discover workflow logs

## What you'll build

![](https://user-images.githubusercontent.com/16547949/62388562-9fc1a500-b52b-11e9-8d7e-4f4d32450fd5.png)

- A working action, including a Dockerfile, an entrypoint script, and a workflow file

## Prerequisites

In this course you will work with issues and pull requests, as well as edit files. If these things are unfamiliar to you, we recommend you take the [Introduction to GitHub]({{ host }}/githubtraining/introduction-to-github) course, first!

## Projects used

The main feature introduced in this course is GitHub Actions. To learn even more, check out the [GitHub Actions feature page](https://github.com/features/actions), or the [GitHub Actions documentation](https://help.github.com/en/actions).

## Audience

Developers, DevOps engineers, students, managers, teams, GitHub users, people interested in automation


---

# Welcome

This course helps you create a simple GitHub Action and use that action in a workflow. 

## What are GitHub Actions?

GitHub Actions are a flexible way to automate nearly every aspect of your team's software workflow. Here are just a few of the ways teams are using GitHub Actions:

- Automated testing (CI)
- Continuous delivery and deployment
- Responding to workflow triggers using issues, @ mentions, labels, and more
- Triggering code reviews
- Managing branches
- Triaging issues and pull requests

The sky is truly the limit with GitHub Actions.

The best part, these workflows are stored as code in your repository and easily shared and reused across teams.

To learn even more, check out the [GitHub Actions feature page](https://github.com/features/actions), or the [GitHub Actions documentation](https://help.github.com/en/actions).

### Before you begin

In this course you will work with issues and pull requests, as well as edit files. If these things are not familiar to you, we recommend you take the [Introduction to GitHub]({{ host }}/githubtraining/introduction-to-github) course, first!


### Actions and Workflows

There are two components to using GitHub Actions that we'll cover:

- the **action** itself
- a **workflow** that uses action(s)

A workflow can contain many actions. Each action has its own purpose. We'll put the files relating to the action in their own directories.

### Types of Actions

Actions come in two types: **container actions** and **JavaScript actions**.

Docker **container actions** allow the environment to be packaged with the GitHub Actions code and can only execute in the GitHub-Hosted Linux environment.

**JavaScript actions** decouple the GitHub Actions code from the environment allowing faster execution but accepting greater dependency management responsibility.

<!--
UNCOMMENT WHEN THESE TWO COURSE GO LIVE AND ADD PROPER LINK DETAILS
📖 To learn more about creating each type of action, refer to the related learning lab course:
  - [Writing JavaScript Actions]()
  - [Writing Docker Container Actions]() -->

## Step 1: Add a `Dockerfile`

Our action will use a Docker container so it will require a `Dockerfile`. Let's add it now. We won't discuss what each line means in detail, but the important thing to know is that the action will be executed in an environment defined by this file.

### :keyboard: Activity: Create a `Dockerfile` and open a pull request

1. Create a file titled `action-a/Dockerfile` by [using this quick link]({{ dockerfileUrl }}) or manually:
   - Create a new branch. _Branches should be named intentionally, so a good name for this branch could be `first-action`_.
   - On the new branch, create a directory: `action-a`. _Note:_ If you're working on GitHub.com, you can create a directory and a file at the same time by naming the file `action-a/Dockerfile`.
   - In the `action-a` directory, create a file titled `Dockerfile`.
1. Fill the `Dockerfile` with the content below:

   ```Dockerfile
   FROM debian:9.5-slim

   ADD entrypoint.sh /entrypoint.sh
   RUN chmod +x /entrypoint.sh
   ENTRYPOINT ["/entrypoint.sh"]
   ```

1. Commit your file
   - If you're working locally, you will also need stage your file and to push the branch to GitHub.
1. Open a pull request with your new branch against `main`

<hr>
<h3 align="center">I'll respond in your new pull request with next steps.</h3>


The Dockerfile isn't where I expected. Here are some troubleshooting steps that might help.

| Problem                                              | Solution                                                                                                                                                                                           |
|------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| The file isn't called `Dockerfile` (case sensitive).  | Rename the file using the [UI](https://help.github.com/articles/renaming-a-file/) or [your CLI](https://help.github.com/articles/renaming-a-file-using-the-command-line/).                         |
| The directory `action-a` doesn't exist.              | [Create the `action-a` folder](https://help.github.com/articles/creating-new-files/) and [move the `Dockerfile`](https://help.github.com/articles/moving-a-file-to-a-new-location/) to `action-a`. |
| The `Dockerfile` isn't inside the `action-a` folder. | [Move the `Dockerfile`](https://help.github.com/articles/moving-a-file-to-a-new-location/) to `action-a`.                                                                                          |

<hr>
<h3 align="center">When I detect your new commit, I'll respond in this pull request.</h3>


Nice work, you committed a `Dockerfile`. You'll notice at the end of the Dockerfile, we refer to an entrypoint script.

```Dockerfile
ENTRYPOINT ["/entrypoint.sh"]
```

The `entrypoint.sh` script will be run in Docker, and it will define what the action is really going to be doing.

## Step 2: Add an entrypoint script

An entrypoint script must exist in our repository so that Docker has something to execute.

### :keyboard: Activity: Add an entrypoint script and commit it to your branch

1. As a part of this branch and pull request, create a file in the `/action-a/` directory titled `entrypoint.sh`. You can do so with [this quicklink]({{ actionAUrl }})
1. Add the following content to the `entrypoint.sh` file:

   ```shell
   #!/bin/sh -l

   sh -c "echo Hello world my name is $INPUT_MY_NAME"
   ```

1. Stage and commit the changes
1. Push the changes to GitHub

<hr>
<h3 align="center">I'll respond when I detect a new commit on this branch.</h3>


The `entrypoint.sh` script isn't where I expected. Here are some troubleshooting steps that might help.

| Problem                                                      | Solution                                                                                                                                                                                          |
| ------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| The file isn't called `entrypoint.sh` (case sensitive).      | Rename the file using the [UI](https://help.github.com/articles/renaming-a-file/) or [your CLI](https://help.github.com/articles/renaming-a-file-using-the-command-line/).                        |
| The directory `action-a` doesn't exist.                      | [Create the `action-a` folder](https://help.github.com/articles/creating-new-files/) and [move `entrypoint.sh`](https://help.github.com/articles/moving-a-file-to-a-new-location/) to `action-a`. |
| The `entrypoint.sh` file isn't inside the `action-a` folder. | [Move `entrypoint.sh`](https://help.github.com/articles/moving-a-file-to-a-new-location/) to `action-a`.                                                                                          |

<hr>
<h3 align="center">When I detect your new commit, I'll respond in this pull request.</h3>


Nice work adding the `entrypoint.sh` script.

In `entrypoint.sh`, all we're doing is outputting a "Hello world" message using an environment variable called `MY_NAME`.

Next, we'll define the `action.yml` file which contains the metadata for our action.

### action.yml

All actions require a metadata file that uses YAML syntax. The data in the metadata file defines the `inputs`, `outputs` and main `entrypoint` for your action.

## Step 3: Add an action metadata file

We will use an `input` parameter to read in the value of `MY_NAME`.

### :keyboard: Activity: Create action.yml

1. As a part of this branch and pull request, create a file titled `action-a/action.yml`. You can do so using [this quicklink]({{ actionAUrl }}) or manually.
1. Add the following content to the `action.yml` file:

   ```yaml
   name: "Hello Actions"
   description: "Greet someone"
   author: "octocat@github.com"

   inputs:
     MY_NAME:
       description: "Who to greet"
       required: true
       default: "World"

   runs:
     using: "docker"
     image: "Dockerfile"

   branding:
     icon: "mic"
     color: "purple"
   ```

1. Stage and commit the changes
1. Push the changes to GitHub

<hr>
<h3 align="center">I'll respond when I detect a new commit on this branch.</h3>


The `action.yml` script isn't where I expected. Here are some troubleshooting steps that might help.

| Problem                                                   | Solution                                                                                                                                                                                       |
| --------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| The file isn't called `action.yml` (case sensitive).      | Rename the file using the [UI](https://help.github.com/articles/renaming-a-file/) or [your CLI](https://help.github.com/articles/renaming-a-file-using-the-command-line/).                     |
| The directory `action-a` doesn't exist.                   | [Create the `action-a` folder](https://help.github.com/articles/creating-new-files/) and [move `action.yml`](https://help.github.com/articles/moving-a-file-to-a-new-location/) to `action-a`. |
| The `action.yml` file isn't inside the `action-a` folder. | [Move `action.yml`](https://help.github.com/articles/moving-a-file-to-a-new-location/) to `action-a`.                                                                                          |

<hr>
<h3 align="center">When I detect your new commit, I'll respond in this pull request.</h3>


Next, we'll define a **workflow** that uses the GitHub Action.

### Workflow Files

Workflows are defined in special files in the `.github/workflows` directory, named `main.yml`.

Workflows can execute based on your chosen event. For this lab, we'll be using the [`push`](https://developer.github.com/v3/activity/events/types/#pushevent) event.

We'll break down each line of the workflow in the next step.

## Step 4: Start your workflow file

First, we'll add the structure of the workflow.

### :keyboard: Activity: Name and trigger your workflow

1. Create a file titled `.github/workflows/main.yml`. You can do so [using this quicklink]({{ worfkflowUrl}}) or manually:
   - As a part of this branch and pull request, create a `workflows` directory nested inside the `.github` directory.
   - In the new `.github/workflows/` directory, create a file titled `main.yml`
1. Add the following content to the `main.yml` file:
   ```yaml
   name: A workflow for my Hello World file
   on: push
   ```
1. Stage and commit the changes
1. Push the changes to GitHub

<details><summary>Trouble pushing? Click here.</summary>

The `main.yml` file cannot be edited using an integration. Try editing the file using the web interface, or your command line.

It is possible that you are using an integration (like GitHub Desktop or any other tool that authenticates as you and pushes on your behalf) if you receive a message like the one below:

```shell
To https://github.com/your-username/your-repo.git
 ! [remote rejected] your-branch -> your-branch (refusing to allow an integration to update main.yml)
error: failed to push some refs to 'https://github.com/your-username/your-repo.git'
```

</details>
<br />

<hr>
<h3 align="center">I'll respond when I detect a new commit on this branch.</h3>


The file `main.yml` isn't where I expected. Here are some troubleshooting steps that might help.

| Problem                                                     | Solution                                                                                                                                                                                        |
|-------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| The file isn't called `main.yml` (case sensitive).      | Rename the file using the [UI](https://help.github.com/articles/renaming-a-file/) or [your CLI](https://help.github.com/articles/renaming-a-file-using-the-command-line/).                       |
| The directory `.github` doesn't exist.                      | [Create the `.github` folder](https://help.github.com/articles/creating-new-files/) and [move `main.yml`](https://help.github.com/articles/moving-a-file-to-a-new-location/) to `.github`. |
| The `main.yml` file isn't inside the `.github` folder. | [Move `main.yml`](https://help.github.com/articles/moving-a-file-to-a-new-location/) to `.github`.                                                                                         |

<hr>
<h3 align="center">When I detect your new commit, I'll respond in this pull request.</h3>


Nice work! :tada: You added a workflow!

Here's what it means:

- `name: A workflow for my Hello World file` gives your workflow a name. This name appears on any pull request or in the Actions tab. The name is especially useful when there are multiple workflows in your repository.
- `on: push` indicates that your workflow will execute anytime code is pushed to your repository, using the [`push`](https://developer.github.com/v3/activity/events/types/#pushevent) event.

Next, we need to specify a job or jobs to run.

### Actions

Workflows piece together jobs, and jobs piece together steps. We'll now create a job that runs an action. Actions can be used from within the same repository, from any other public repository, or from a published Docker container image. We'll use an action that we'll define in this repository.

We'll add the block now, and break it down in the next step.

## Step 5: Run an action from your workflow file

Let's add the expected action to the workflow.

### :keyboard: Activity: Add an action block to your workflow file

1. As a part of this branch and pull request, [edit `.github/workflows/main.yml`]({{ workflowEditUrl }}) to append the following content:
   ```yaml
   jobs:
     build:
       name: Hello world action
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v1
         - uses: ./action-a
           with:
             MY_NAME: "Mona"
   ```
1. Click **Start commit** in the top right of the workflow editor
1. Type your commit message and commit your changes directly to your branch

<details><summary>Trouble pushing?</summary>

The `main.yml` file cannot be edited using an integration. Try editing the file using the web interface, or your command line.

It is possible that you are using an integration (like GitHub Desktop or any other tool that authenticates as you and pushes on your behalf) if you receive a message like the one below:

```shell
To https://github.com/your-username/your-repo.git
 ! [remote rejected] your-branch -> your-branch (refusing to allow an integration to update main.yml)
error: failed to push some refs to 'https://github.com/your-username/your-repo.git'
```

</details>
<br />

<hr>
<h3 align="center">I'll respond when I detect a new commit on this branch.</h3>


The file `main.yml` isn't where I expected. Here are some troubleshooting steps that might help.

| Problem                                                     | Solution                                                                                                                                                                                        |
|-------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| The file isn't called `main.yml` (case sensitive).      | Rename the file using the [UI](https://help.github.com/articles/renaming-a-file/) or [your CLI](https://help.github.com/articles/renaming-a-file-using-the-command-line/).                       |
| The directory `.github` doesn't exist.                      | [Create the `.github` folder](https://help.github.com/articles/creating-new-files/) and [move `main.yml`](https://help.github.com/articles/moving-a-file-to-a-new-location/) to `.github`. |
| The `main.yml` file isn't inside the `.github` folder. | [Move `main.yml`](https://help.github.com/articles/moving-a-file-to-a-new-location/) to `.github`.                                                                                         |

<hr>
<h3 align="center">When I detect your new commit, I'll respond in this pull request.</h3>


Nice, you just added an action block to your workflow file! Here are some important details about _why_ each part of the block exists and _what_ each part does.

- `jobs:` is the base component of a workflow run
- `build:` is the identifier we're attaching to this job
- `name:` is the name of the job, this is displayed on GitHub when the workflow is running
- `runs-on:` defines the type of machine to run the job on. The machine can be either a GitHub-hosted runner or a self-hosted runner.
- `steps:` the linear sequence of operations that make up a job
- `uses: actions/checkout@v1` uses a community action called [`checkout`](https://github.com/actions/checkout) to allow the workflow to access the contents of the repository
- `uses: ./action-a` provides the relative path to the action we created in the `action-a` directory of the repository
- `with`: is used to specify the input variables that will be available to your action in the runtime environment. In this case, the input variable is `MY_NAME`, and it is currently initialized to `"Mona"`.

### Your action has been triggered!

Your repository now contains an action (defined in the `/action-a/` folder) and a workflow (defined in the `./github/workflows/main.yml` file).

This action will run any time a new commit is created or pushed to the remote repository. Since you just created a commit, the workflow should have been triggered. This might take a few minutes since it's the first time running in this repository.

### Seeing your Action in action

The status of your action is shown here in the pull request (look for **All checks have passed** below), or you can click the "Actions" tab in your repository. From there you will see the actions that have run, and you can click on the action's "Log" link to view details.

![View an action's log](https://user-images.githubusercontent.com/16547949/62388049-4e64e600-b52a-11e9-8bf5-db0c5452360f.png)

## Step 6: Trigger the workflow

### :keyboard: Activity: See your action trigger the workflow

You've done the work, now sit back and see your action trigger the workflow!

<hr>
<h3 align="center">I will respond when I detect your action has run and reported a status.</h3>

> _Actions can take a minute or two to run. Sometimes, I also respond too fast for the page to update! If you don't see a response from your action, wait a few seconds and refresh the page._


Almost there, but the workflow didn't run.

Here's some possible reasons why:
- files aren't in proper directories
- your script isn't executable

### Troubleshooting steps

Check out the action's output in the [Actions tab]({{ repo }}/actions).

You can also use the following to help you troubleshoot:
<details><summary>For <code>/action-a/entrypoint.sh</code></summary>

| Problem                                                      | Solution                                                                                                                                                                                          |
|--------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `entrypoint.sh` isn't executable.                             | In your shell, run `chmod +x action-a/entrypoint.sh` on this branch and push it up to GitHub.                                                                                                     |
| The file isn't called `entrypoint.sh` (case sensitive).       | Rename the file using the [UI](https://help.github.com/articles/renaming-a-file/) or [your CLI](https://help.github.com/articles/renaming-a-file-using-the-command-line/).                         |
| The directory `action-a` doesn't exist.                      | [Create the `action-a` folder](https://help.github.com/articles/creating-new-files/) and [move `entrypoint.sh`](https://help.github.com/articles/moving-a-file-to-a-new-location/) to `action-a`. |
| The `entrypoint.sh` file isn't inside the `action-a` folder. | [Move `entrypoint.sh`](https://help.github.com/articles/moving-a-file-to-a-new-location/) to `action-a`.                                                                                          |
</details>

<details><summary>For <code>/action-a/Dockerfile</code></summary>

| Problem                                              | Solution                                                                                                                                                                                           |
|------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| The file isn't called `Dockerfile` (case sensitive).  | Rename the file using the [UI](https://help.github.com/articles/renaming-a-file/) or [your CLI](https://help.github.com/articles/renaming-a-file-using-the-command-line/).                          |
| The directory `action-a` doesn't exist.              | [Create the `action-a` folder](https://help.github.com/articles/creating-new-files/) and [move the `Dockerfile`](https://help.github.com/articles/moving-a-file-to-a-new-location/) to `action-a`. |
| The `Dockerfile` isn't inside the `action-a` folder. | [Move the `Dockerfile`](https://help.github.com/articles/moving-a-file-to-a-new-location/) to `action-a`.                                                                                          |
</details>

<details><summary>For <code>.github/workflows/main.yml</code></summary>

| Problem                                                     | Solution                                                                                                                                                                                        |
|-------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| There's some problem with your syntax in `main.yml`.   | Copy and paste the code exactly as is shown in this PR (check for extra spaces, symbols) or see if an error appears in the action logs.                                                         |
| The file isn't called `main.yml` (case sensitive).      | Rename the file using the [UI](https://help.github.com/articles/renaming-a-file/) or [your CLI](https://help.github.com/articles/renaming-a-file-using-the-command-line/).                       |
| The directory `.github/workflows` doesn't exist.                      | [Create the `.github/workflows` folders](https://help.github.com/articles/creating-new-files/) and [move `main.yml`](https://help.github.com/articles/moving-a-file-to-a-new-location/) to `.github/workflows`. |
| The `main.yml` file isn't inside the `.github/workflows` folder. | [Move `main.yml`](https://help.github.com/articles/moving-a-file-to-a-new-location/) to `.github/workflows`.                                                                                         |
</details>

<hr>
<h3 align="center">Next time you commit, your action will try to run. I'll respond when that occurs.</h3>


Success! :tada: Your workflow ran! [You can see the output here]({{ repo }}/actions).

You should see the string "Hello world, I'm Mona!" printed at the bottom to `stdout`.

![Actions successful log file](https://user-images.githubusercontent.com/16547949/62388562-9fc1a500-b52b-11e9-8d7e-4f4d32450fd5.png)

## Step 7: Incorporate the workflow

As a final step, merge this pull request so the action will be a part of the `main` branch.

Anyone that uses this repository, and any future code can benefit from this workflow and your new action!

### :keyboard: Activity: Merge your workflow into the `main` branch

1. Merge this pull request
1. Delete your branch

<hr>
<h3 align="center">I'll respond when I detect this branch has been merged.</h3>


## Nice work!

![celebrate](https://octodex.github.com/images/jetpacktocat.png)

You've created your first GitHub Action and this course is now complete! I'll stop responding but the fun doesn't have to stop here.

## Want to keep learning?

<!-- Continue learning about actions by taking the next course in the [GitHub Actions Learning Path]() -->

In this repository:

- Your merge should trigger your action again, check it out in the [Actions tab]({{ repo }}/actions).
- The `Dockerfile` contains metadata for your action. Try changing some of that. You could, for example, change the icon that displays when the action is running.
- Change the `MY_NAME` environment variable to use your name instead of Mona's in `.github/workflows/main.yml`.
- Change the contents of `entrypoint.sh` to output a different message.

Outside of this repository:

- Review the [GitHub Actions documentation](https://docs.github.com/actions/learn-github-actions) on the GitHub Developer site.
- Use existing actions from the [GitHub Marketplace](https://github.com/marketplace/actions).
- Use existing actions from GitHub's [official actions community](https://github.com/actions).
- Use actions created by others in [awesome-actions](https://github.com/sdras/awesome-actions).

Now...[what will you learn next]({{ host }}/courses)?


<hr>
<h3 align="center">Great work merging your pull request! I created a <a href="{{ url }}">new issue</a>, look for my final response there.</h3>


