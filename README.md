<header>

# Hello GitHub Actions

_Create and run a GitHub Actions workflow._

</header>

## Welcome

Automation is key for streamlining your work processes, and [GitHub Actions](https://docs.github.com/actions) is the best way to supercharge your workflow.

- **Who is this for**: Developers, DevOps engineers, students, managers, teams, GitHub users.
- **What you'll learn**: How to create workflow files, trigger workflows, and find workflow logs.
- **What you'll build**: An Actions workflow that will check emoji shortcode references in Markdown files.
- **Prerequisites**: In this course you will work with issues and pull requests, as well as edit files. We recommend you take the [Introduction to GitHub](https://github.com/skills/introduction-to-github) course first.
- **How long**: This course can be finished in less than two hours.

In this course, you will:

1. Create a workflow
2. Add a job
3. Add a run step
4. Merge your pull request
5. See effect of the workflow

### How to start this course

[![start-course](https://user-images.githubusercontent.com/1221423/235727646-4a590299-ffe5-480d-8cd5-8194ea184546.svg)](https://github.com/new?template_owner=skills&template_name=hello-github-actions&owner=%40me&name=skills-hello-github-actions&description=My+clone+repository&visibility=public)

1. Right-click **Start course** and open the link in a new tab.
2. In the new tab, most of the prompts will automatically fill in for you.
   - For owner, choose your personal account or an organization to host the repository.
   - We recommend creating a public repository, as private repositories will [use Actions minutes](https://docs.github.com/en/billing/managing-billing-for-github-actions/about-billing-for-github-actions).
   - Scroll down and click the **Create repository** button at the bottom of the form.
3. After your new repository is created, wait about 20 seconds, then refresh the page. Follow the step-by-step instructions in the new repository's README.

<footer>

---

Get help: [Post in our discussion board](https://github.com/orgs/skills/discussions/categories/hello-github-actions) &bull; [Review the GitHub status page](https://www.githubstatus.com/)

&copy; 2023 GitHub &bull; [Code of Conduct](https://www.contributor-covenant.org/version/2/1/code_of_conduct/code_of_conduct.md) &bull; [MIT License](https://gh.io/mit)

</footer>
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cardápio Futurista - Daniella Sapatinho</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background-color: #0d0d0d;
            color: #fff;
            margin: 0;
            padding: 0;
        }
        header {
            background: #222;
            padding: 20px;
            text-align: center;
        }
        header h1 {
            font-size: 2.5em;
            margin: 0;
        }
        section {
            padding: 20px;
        }
        .menu-category {
            margin-bottom: 40px;
        }
        .menu-category h2 {
            font-size: 1.8em;
            border-bottom: 2px solid #6a6a6a;
            padding-bottom: 5px;
            margin-bottom: 20px;
        }
        .menu-item {
            display: flex;
            justify-content: space-between;
            margin-bottom: 15px;
            padding: 10px;
            background-color: #333;
            border-radius: 8px;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
        }
        .menu-item img {
            width: 50px;
            height: 50px;
            object-fit: cover;
            border-radius: 8px;
        }
        .item-description {
            flex: 1;
            margin-left: 20px;
        }
        .item-name {
            font-size: 1.2em;
        }
        .item-price {
            font-size: 1.2em;
            font-weight: bold;
        }
    </style>
</head>
<body>

<header>
    <h1>Daniella Sapatinho</h1>
    <p>Cardápio Futurista</p>
</header>

<section>
    <div class="menu-category">
        <h2>Pratos Principais</h2>
        <div class="menu-item">
            <img src="https://example.com/filé-mignon.jpg" alt="Filé Mignon">
            <div class="item-description">
                <div class="item-name">Filé Mignon</div>
                <div class="item-price">R$ 80,00</div>
            </div>
        </div>
        <div class="menu-item">
            <img src="https://example.com/salmão.jpg" alt="Salmão">
            <div class="item-description">
                <div class="item-name">Salmão Grelhado</div>
                <div class="item-price">R$ 95,00</div>
            </div>
        </div>
    </div>

    <div class="menu-category">
        <h2>Sobremesas</h2>
        <div class="menu-item">
            <img src="https://example.com/sobremesa1.jpg" alt="Sobremesa 1">
            <div class="item-description">
                <div class="item-name">Torta de Chocolate</div>
                <div class="item-price">R$ 20,00</div>
            </div>
        </div>
        <div class="menu-item">
            <img src="https://example.com/sobremesa2.jpg" alt="Sobremesa 2">
            <div class="item-description">
                <div class="item-name">Sorvete de Baunilha</div>
                <div class="item-price">R$ 15,00</div>
            </div>
        </div>
    </div>
</section>

</body>
</html>
