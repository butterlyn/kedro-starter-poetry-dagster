# Update source code

1. Serve documentation locally
    ```
    poetry run mkdocs serve
    ```
    By default, this will serve the documentation at [http://localhost:8000](http://localhost:8000).
2. Launch the Kedro Viz dashboard
    ```
    poetry run kedro viz run --autoreload
    ```
    By default, this will serve the dashboard at [http://localhost:4141](http://localhost:4141).

    !!! note
        All three of these can be run with ```poetry run python ./scripts/launch.py```

3. Launch the Dagster dashboard
    ```
    poetry run dagit
    ```
    By default, this will serve the dashboard at [http://localhost:3000](http://localhost:3000).
4. Change source code, including docstrings
    1. Static type-checking
    ```
    poetry run mypy
    ```
    2. Add or remove dependencies
    ```
    poetry add <package name>
    ```
    ```
    poetry remove <package name>
    ```
    3. run tests
    ```
    poetry run pytest
    ```