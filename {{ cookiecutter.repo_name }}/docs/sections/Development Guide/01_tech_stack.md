# Technology Stack

- [x] Dependency management:
    - [x] [Poetry](https://python-poetry.org/)
    - [x] Python version management:
        - [x] [pyenv](https://github.com/pyenv/pyenv)
        - [x] [Conda + Poetry](https://medium.com/@silvinohenriqueteixeiramalta/conda-and-poetry-a-harmonious-fusion-8116895b6380)
- [ ] Packaging
    - [ ] Poetry publishing to Azure Arifacts
    - [x] Kedro packaging: [Package an entire Kedro project](https://docs.kedro.org/en/stable/tutorial/package_a_project.html)
    - [ ] Kedro micropackaging: [Kedro micro-packaging](https://docs.kedro.org/en/stable/nodes_and_pipelines/micro_packaging.html)
    - [ ] Hydra packaging: [Hydra application packaging](https://hydra.cc/docs/advanced/app_packaging/)
- [x] Package structure: [Kedro](https://kedro.org/)
    - [x] Templating: [Kedro Starters](https://docs.kedro.org/en/latest/starters/create_a_starter.html)
- [x] DAG visualisation: [Kedro Viz](https://docs.kedro.org/en/latest/visualisation/index.html)
- [x] Orchestration: [Dagster](https://dagster.io/)
    - [ ] SQL models: [dbt + Dagster](https://docs.dagster.io/integrations/dbt)
        - [ ] Locally-run SQL models: [dbt + DuckDB](https://docs.getdbt.com/docs/core/connect-data-platform/duckdb-setup)
- [ ] Integrations:
    - [ ] Databricks integration:
        - [ ] Databricks + Kedro: [How to integrate Kedro and Databricks Connect](https://kedro.org/blog/managed-delta-tables-kedro-dataset)
        - [ ] Databricks + Dagster: [Using Databricks with Dagster](https://docs.dagster.io/integrations/databricks)
    - [ ] Deltalake integration:
        - [ ] Delta Lake + Dagster: [Delta Lake + Dagster](https://docs.dagster.io/integrations/deltalake)
        - [ ] Delta Lake + Kedro: [How to use Databricks managed Delta tables in a Kedro project](https://kedro.org/blog/managed-delta-tables-kedro-dataset)
    - [ ] Oracle integration:
        - [ ] Oracle + Kedro: [pandas.SQLQueryDataset](https://docs.kedro.org/projects/kedro-datasets/en/kedro-datasets-2.0.0/api/kedro_datasets.pandas.SQLQueryDataset.html#kedro_datasets.pandas.SQLQueryDataset)
        - [ ] Oracle + dbt (+ Dagster): [Oracle + Dagster](https://docs.getdbt.com/docs/core/connect-data-platform/oracle-setup)
- [ ] Exploratory data analysis:
    - [x] Jupyter notebooks: [JupyterLab](https://jupyterlab.readthedocs.io/en/stable/)
        - [ ] Interactive pivot tables: [Pygwalker](https://docs.kanaries.net/pygwalker)
        - [ ] Automated analysis: [Lux](https://lux-api.readthedocs.io/en/latest/)
- [x] Formatting: [Ruff](https://github.com/astral-sh/ruff)
- [x] Linting: [Flake8](https://flake8.pycqa.org/en/latest/)
- [x] Static type checking: [mypy](https://mypy.readthedocs.io/en/stable/index.html)
- [x] Documentation: [mkdocs](https://www.mkdocs.org/), [mkdocs-material](https://squidfunk.github.io/mkdocs-material/)
    - [ ] Versioning: [mike](https://github.com/jimporter/mike), [mike in mkdocs-material](https://squidfunk.github.io/mkdocs-material/setup/setting-up-versioning/)
    - [ ] API documentation generation: [mkdocstrings](https://mkdocstrings.github.io/), [material recipe](https://mkdocstrings.github.io/recipes/#generate-pages-on-the-fly)
        - [ ] Pydantic documentation generation: [griffe-pydantic](https://mkdocstrings.github.io/griffe-pydantic/)
    - [ ] Diagram rendering:
        - [x] Mermaid:
            - [x] Data flow diagram rendering: [mermaid](https://mermaid.js.org/)
            - [x] Mermaid + mkdocs-material: [mkdocs-material diagrams](https://squidfunk.github.io/mkdocs-material/reference/diagrams/)
        - [ ] PlantUML:
            - [x] PlantUML + mkdocs: [mkdocs_puml](https://github.com/MikhailKravets/mkdocs_puml)
            - [x] Activity (flowchart) diagram rendering: [plantuml](https://plantuml.com/activity-diagram-beta)
            - [ ] Configuration rendering: [plantuml display json data](https://plantuml.com/json), [plantuml display yaml data](https://plantuml.com/yaml)
    - [x] Maths rendering: [KaTeX](https://katex.org/), [KaTeX in mkdocs-material](https://squidfunk.github.io/mkdocs-material/reference/math/#katex)
    - [ ] Azure deployment: [Azure Static Web Apps](https://docs.microsoft.com/en-us/azure/static-web-apps/)
        - [x] [Azure Static Web Apps: configuration file](https://learn.microsoft.com/en-us/azure/static-web-apps/configuration#file-location)
        - [x] [Azure Static Web Apps: configure with Microsoft Entra ID](https://learn.microsoft.com/en-us/azure/static-web-apps/authentication-custom?tabs=aad%2Cinvitations#microsoft-entra-version-2)
        - [x] [Azure Static Web Apps: restrict access to entire application](https://learn.microsoft.com/en-us/azure/static-web-apps/configuration#restrict-access-to-entire-application)
        - [x] [Azure Static Web Apps: redirect to login page](https://learn.microsoft.com/en-us/azure/static-web-apps/authentication-authorization#set-up-post-sign-in-redirect)
        - [x] [Azure Static Web Apps: deploy with Azure Pipelines](https://learn.microsoft.com/en-us/azure/devops/pipelines/tasks/reference/azure-static-web-app-v0?view=azure-pipelines)
- [ ] Command line interface:
    - [ ] Running model multiruns [hydra](https://hydra.cc/)
    - [ ] Development: [Nox](https://nox.thea.codes/en/stable/), [nox-poetry](https://github.com/cjolowicz/nox-poetry)
- [ ] Testing: [pytest](https://docs.pytest.org/)
    - [ ] Coverage: [pytest-cov](https://pytest-cov.readthedocs.io/en/latest/)
    - [ ] Edge-case: [Polars testing with hypothesis](https://docs.pola.rs/py-polars/html/reference/testing.html), [Hypothesis](https://hypothesis.readthedocs.io/en/latest/)
    - [ ] Kedro testing: [Kedro testing](https://docs.kedro.org/en/latest/development/automated_testing.html)
    - [ ] Dagster testing: [Dagster testing](https://docs.dagster.io/concepts/testing), [Dagster testing assets](https://docs.dagster.io/guides/dagster/testing-assets)
- [ ] Memory profiler: [Memray](https://bloomberg.github.io/memray/index.html)
- [ ] Dataframes: [Polars](https://docs.pola.rs/user-guide/)
    - [ ] Plugin for Dagster: [Dagster Polars](https://github.com/danielgafni/dagster-polars)
    - [ ] Plugin for Kedro: [Kedro Datasets Polars](https://docs.kedro.org/projects/kedro-datasets/en/kedro-datasets-2.0.0/api/kedro_datasets.polars.LazyPolarsDataset.html)
    - [ ] Plugin for LightGBM: [functime](https://functime.ai/)
- [ ] Validation:
    - [ ] Configuration validation: [Pydantic](https://docs.pydantic.dev/1.10/) (pinned to verion 1 due to compatibility issues with Kedro Viz)
    - [ ] DataFrame validation: [Pandera DataFrame Models](https://pandera.readthedocs.io/en/stable/dataframe_models.html)
- [ ] Plotting: [Plotly](https://plotly.com/python/)
    - [ ] Integration with Kedro Viz: [Kedro Plotly](https://docs.kedro.org/projects/kedro-viz/en/stable/visualise_charts_with_plotly.html)
    - [ ] Integration with Polars: [Polars Plot](https://docs.pola.rs/py-polars/html/reference/dataframe/plot.html#), [hvPlot](https://hvplot.holoviz.org/reference/index.html)
- [ ] Versioning: [git](https://git-scm.com/)
    - [ ] Semantic versioning: [SemVer 2.0.0](https://semver.org/)
    - [ ] Branching model: [GitHub Flow](https://www.atlassian.com/git/tutorials/comparing-workflows/feature-branch-workflow)
    - [ ] Merging: [Merging option](https://www.atlassian.com/git/tutorials/merging-vs-rebasing)
- [ ] CI/CD: [Azure Pipeline](https://azure.microsoft.com/en-us/services/devops/pipelines/)
- [ ] Containerisation: [Docker](https://www.docker.com/)
    - [ ] Containerising Kedro projects: [Kedro Docker](https://github.com/kedro-org/kedro-plugins/tree/main/kedro-docker)
    - [ ] Containerising Dagster projects: [Dagster Docker](https://docs.dagster.io/deployment/guides/docker)