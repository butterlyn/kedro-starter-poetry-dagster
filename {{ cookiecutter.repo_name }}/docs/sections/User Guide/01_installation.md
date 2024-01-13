# Installation

## Requirements

1. Install python with [pyenv](https://github.com/pyenv/pyenv) (on windows: [pyenv-win](https://github.com/pyenv-win/pyenv-win))
2. Install [Poetry](https://python-poetry.org/docs/#installation)
3. Set the python version with `pyenv`, install if necessary.
    ``` title = "Set python version with pyenv"
    pyenv install <python_version>
    ```
    ``` title = "Set the version of python for the current directory"
    pyenv local <python_version>
    ```
3. Install dependencies with Poetry
    ```
    poetry install
    ```

!!! note
    To run commands in this environment, use `poetry run <command>`.

### Alternative - Conda

If using conda instead of step 1 and step 2:

1. Install [conda](https://docs.conda.io/en/latest/miniconda.html)
2. Install conda environment (substitute `<env_name>` with desired environment name, e.g. `my_project`). 
    ```
    conda env create --file ./environment.yml --name <env_name>
    ```
    This will install python and poetry, but no dependencies.
3. Activate conda environment
    ```
    conda activate <env_name>
    ```
3. Install dependencies with Poetry
    ```
    poetry install
    ```

!!! warning
    If using conda and Poetry, new dependencies should be [managed with Poetry](https://python-poetry.org/docs/managing-dependencies/) in `pyprojec.toml` file, NOT in the `environment.yml` file.
