import subprocess
import os
from pathlib import PosixPath
from typing import Any
from pathlib import Path
import polars as pl
from kedro.framework.session import KedroSession
from kedro.framework.startup import bootstrap_project
from kedro.config import OmegaConfigLoader
from kedro.framework.project import settings
import click
from dagster import (
    asset,
    Config,
)

# load Kedro project metadata
config_file: PosixPath
package_name: str
project_name: str
project_path: PosixPath
project_version: str
source_dir: PosixPath
(
    config_file,
    package_name,
    project_name,
    project_path,
    project_version,
    source_dir,
    kedro_init_version,
) = bootstrap_project(Path.cwd())

# load Kedro parameters stored in conf/base/
conf_path: str = str(project_path / settings.CONF_SOURCE)
conf_loader: OmegaConfigLoader = OmegaConfigLoader(conf_source=conf_path)
parameters: dict[str, Any] = conf_loader["parameters"]

# set these Kedro parameters as the default Dagster config
PipelineConfig: Config = type(
    'PipelineConfig',
    (Config,),
    parameters,
)


@asset(name=package_name)
def kedro_project_as_dagster_asset(config: PipelineConfig) -> dict[str, Any]:
    bootstrap_project(Path.cwd())
    with KedroSession.create() as session:
        outputs: dict[str, Any] = session.run()
        return {
            key:
                value.collect(streaming=True)
                if isinstance(value, pl.LazyFrame)
                else value
            for key, value
            in outputs.items()
        }


@click.command()
@click.option(
    '--port',
    type=int,
    default=3000,
    help='Port number to run Dagster on',
)
def run_dagster_dashboard(port):
    # get the path of this python script
    script_path = os.path.realpath(__file__)

    # command to run
    command = f"dagster dev --python-file {script_path} --port {port}"

    # run the command
    process = subprocess.Popen(command, shell=True)

    # wait for the command to complete
    output, error = process.communicate()

    return output, error


if __name__ == "__main__":
    run_dagster_dashboard()
