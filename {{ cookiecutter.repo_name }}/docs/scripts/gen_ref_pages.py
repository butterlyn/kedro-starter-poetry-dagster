# pylint: disable=all
"""
Generates API documentation that can be referenced in mkdocs
mkdocs.yml using:

=== "yaml"
    ```yaml
    nav:
        - API Reference: reference/
    ```

!!! note
    Modules can be excluded from API documentation using a leading underscore
    in the file name.

!!! note
    __all__ in __init__.py specifies what function or classes are
    included in the API documentation.

!!! info "References"
    Script was derived from [mkdocstrings recipe](https://mkdocstrings.github.io/recipes/)
"""
from pathlib import Path

import mkdocs_gen_files

nav = mkdocs_gen_files.Nav()

src = Path(__file__).parent.parent.parent / "src"

mermaid_blocks = []

for path in sorted(src.rglob("*.py")):
    # If the directory of the current file starts with an underscore, skip it
    if path.parts[-2].startswith("_"):
        continue
    module_path = path.relative_to(src)
    module_path_without_suffix = module_path.with_suffix("")
    doc_path = path.relative_to(src).with_suffix(".md")
    full_doc_path = Path("reference", doc_path)

    parts = tuple(module_path_without_suffix.parts)

    # rename __init__.py files to <package name>.md
    is_init: bool = False
    if parts[-1] == "__init__":
        is_init = True
        parts = parts[:-1]
        doc_path = doc_path.with_stem("index").with_suffix(".md")
        full_doc_path = full_doc_path.with_stem("index").with_suffix(".md")

        # Open the __init__.py file and search for mermaid code blocks
        with open(path, "r") as file:
            lines = file.readlines()
            mermaid_block: list = []
            recording = False
            for line in lines:
                if "```mermaid" in line:
                    recording = True
                elif "```" in line and recording:
                    recording = False
                    # Filter out lines with 'flowchart TD'
                    filtered_block = [
                        lin
                        for lin in mermaid_block
                        if "flowchart TD" not in lin
                        and "flowchart LR" not in lin
                    ]
                    mermaid_blocks.append("\n".join(filtered_block))
                    mermaid_block = []
                elif recording:
                    mermaid_block.append(line.strip())

    # skip __main__.py files
    elif parts[-1] == "__main__":
        continue
    elif parts[-1] == "settings":
        continue
    elif parts[-1] == "pipeline_registry":
        continue
    # filter out private modules (i.e., those starting with _)
    elif parts[-1].startswith("_"):
        continue

    nav[parts] = doc_path.as_posix()

    # Define the content of the page
    with mkdocs_gen_files.open(full_doc_path, "w") as fd:
        IDENT = ".".join(parts)
        title = (
            f"# {doc_path.parent.name}"
            if is_init
            else f"# {doc_path.with_suffix('').name}"
        )

        fd.write(f"{title}\n")
        fd.write(f"::: {IDENT}")

    mkdocs_gen_files.set_edit_path(full_doc_path, path)

with mkdocs_gen_files.open("reference/SUMMARY.md", "w") as nav_file:
    nav_file.writelines(nav.build_literate_nav())

# After all files have been processed, write the mermaid blocks to a page in mkdocs
with mkdocs_gen_files.open("reference/mermaid.md", "w") as mermaid_file:
    mermaid_file.write("```mermaid\n")
    mermaid_file.write("flowchart LR\n")
    mermaid_file.write("\n".join(mermaid_blocks))
    mermaid_file.write("\n```\n")
    mermaid_file.write(
        "``` title='To zoom in or edit, go to this website and copy the script below: https://mermaid.live/'\n"
    )
    mermaid_file.write("flowchart LR\n")
    mermaid_file.write("\n".join(mermaid_blocks))
    mermaid_file.write("\n```\n")
