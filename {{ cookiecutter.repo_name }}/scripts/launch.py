"""Launch the developer environment for the project."""


import subprocess

# Define the commands to be run
commands = [
    "poetry run python ./scripts/launch_dagster.py",
    "poetry run kedro viz run --autoreload",
    "poetry run mkdocs serve",
]

# Define the ports associated with each command
ports = [4141, 4000, 8000]

# Run each command as a subprocess
for command, port in zip(commands, ports):
    print(f"Running command: {command}")
    subprocess.Popen(command, shell=True)
    print(f"Open localhost at port: {port}")
