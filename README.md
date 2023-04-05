# DSCoV-ModernPython

This repo contains a very simple Python package that can be built with Poetry and published to PyPI.

Please clone this repo and follow along:

```bash
git clone https://github.com/brown-ccv/DSCoV-ModernPython.git
```

## Modern Python Part 1: Modern Project Management

### 1. Install Poetry

There are many ways to install Poetry, but it is highly recommended that you install poetry in its own virtual environment so it is isolated from other projects that you are running. The official and recommended way of doing this is to download its installation script on its official website:

**_NOTE:_**  make sure that you are not running this command in any virtual environment.

On MacOS/Linux, you can run this in your terminal:

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

You can also install Poetry with `homebrew`:

```bash
brew install poetry
```

On Windows, you can run this in your PowerShell:

```powershell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
```

After installation, you can check your poetry installation by running:

```bash
poetry --version
```

### 2. Create a project with Poetry

Creating a project with Poetry is easy. Simply run:

```bash
poetry new my_package
```

It will create a directory with the name `my_package` with the standard structure. The directory will look like this:

```
my_package
├── pyproject.toml
├── README.md
├── my_package
│   └── __init__.py
└── tests
    └── __init__.py
```

If you want to have a different name for the directory than for the package, do this:

```bash
poetry new my_folder --name my_package
```

Usually it's good to have your source code under the `src` directory. To to so, do this:

```bash
poetry new --src my_package
```

And the folder will look like this:

```
my_package
├── pyproject.toml
├── README.md
├── src
│   └── my_package
│       └── __init__.py
└── tests
    └── __init__.py
```

You can also initialize your project from an existing directory. You can run `poetry init` from the directory. There will be an interactive guide that walks you through the creation of the project.

### 3. Manage dependencies

We now know how to start new project with Poetry. However, what Poetry really does well is how it manages dependencies for existing projects. To see how Poetry does this, let's **start a new terminal** and clone this repo:

```bash
git clone https://github.com/brown-ccv/DSCoV-ModernPython.git && cd DSCoV-ModernPython
```

#### 3.1 `poetry install`

This is a simple package similar to `cowsay`. The only difference is that instead of a cow, it prints out a dragon. To run this package, we typically need to create a virtual environment, install its dependencies in a virtual environment, and then install this package in this virtual environment. Poetry makes it so easy that we can do all these with one command:

```bash
poetry install
```

After cloning the repo, you can run `poetry install` in the directory. Poetry will create a virtual environment, install all dependencies, and the current Python package.

We can verify the packages installed in the environment by using `poetry show`.

#### 3.2 `poetry run` and `poetry shell`

You can run any command from within the environment by using `poetry run`. For example, now that we have installed our package to the virtual environment, we can run

```bash
poetry run dragonsay fire!
```

Alternatively you can also activate the environment by using `poetry shell`. Then you can run the same command without `poetry run`.

#### 3.3 `poetry add`, `poetry remove`, and `poetry update`

Dependencies can be added/removed by using `poetry add`/`poetry remove`. It is also possible to specify versions:

```bash
poetry add pandas==2.0.0
```

You can also use `poetry update` to update all dependencies or specify the packages that you want to update:

```bash
poetry update numpy
```

### Build and publish your project

It's very easy to build a project into a package and publish it. The only thing you need to do is to specify your build tools in `pyproject.toml`:

```toml
[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
```

Poetry has its own build tools, but there are also other build tools that you can use, such as `hatchling`, `setuptools`, `cython` etc. With these specifications, you can simply run

```bash
poetry build
```

Publishing packages to the Python Package Index (PyPI) is also very simple. Let us try publishing our little package to [TestPyPI](https://test.pypi.org). TestPyPI is the test version of PyPI, which allows us to test if we can publish packages to PyPI. Before we do that, let's register on [TestPyPI](https://test.pypi.org).

After getting an account, click on your username on the top right corner of the page, and choose "Account Settings". Then, in "Account Settings", hit "Add API Token" to get an API token for your TestPyPI page.

**NOTE**: You might want your package to be under a different name since I have already published `dragonsay`. Simply change the name of the project in `pyproject.toml` to a different one.

Now do the following steps:

```bash
poetry config repositories.testpypi https://test.pypi.org/legacy/
poetry config pypi-token.testpypi <your-testpypi-token>

poetry publish -r testpypi
```

**NOTE**: It's even simpler to publish to the real PyPI. You only need to specify the real PyPI token:


```bash
poetry config pypi-token.pypi <your-testpypi-token>

poetry publish
```
