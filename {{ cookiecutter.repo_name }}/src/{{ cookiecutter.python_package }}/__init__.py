"""{{ cookiecutter.project_name }}"""


import importlib.metadata

# extract package version from pyproject.toml
__version__ = importlib.metadata.version(__name__)
