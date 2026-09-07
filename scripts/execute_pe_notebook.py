"""Execute the pure-Python reproduction notebook without opening Jupyter ports.

Useful in restricted offline environments. Every code cell is actually executed;
stdout/stderr, errors, execution counts, and the runner are recorded in the file.
For an interactive kernel, open the same notebook in Jupyter instead.
"""

from __future__ import annotations

import io
import traceback
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path

import nbformat


def main():
    path = Path(__file__).resolve().parent / "notebooks/pe-computed-numbers.ipynb"
    notebook = nbformat.read(path, as_version=4)
    notebook.metadata["execution_backend"] = (
        "in-process Python; no Jupyter server or sockets"
    )
    namespace = {"__name__": "__main__"}
    for i, cell in enumerate(notebook.cells):
        if cell.cell_type == "code":
            cell.outputs = []
            cell.execution_count = None
    count = 0
    for i, cell in enumerate(notebook.cells):
        if cell.cell_type != "code":
            continue
        count += 1
        print(f"Executing notebook cell {i + 1} ({count})", flush=True)
        output, errors = io.StringIO(), io.StringIO()
        failure = None
        with redirect_stdout(output), redirect_stderr(errors):
            try:
                exec(  # noqa: S102 -- execute this repository's trusted notebook
                    compile(cell.source, f"{path.name}:cell-{i + 1}", "exec"), namespace
                )
            except Exception as exc:  # noqa: BLE001 -- record and re-raise every failure
                failure = exc
                failure_trace = traceback.format_exc()
        cell.execution_count = count
        for name, stream in (("stdout", output), ("stderr", errors)):
            if stream.getvalue():
                cell.outputs.append(
                    nbformat.v4.new_output("stream", name=name, text=stream.getvalue())
                )
                print(stream.getvalue(), end="", flush=True)
        if failure is not None:
            cell.outputs.append(
                nbformat.v4.new_output(
                    "error",
                    ename=type(failure).__name__,
                    evalue=str(failure),
                    traceback=failure_trace.splitlines(),
                )
            )
        nbformat.validate(notebook)
        nbformat.write(notebook, path)
        if failure is not None:
            raise failure
    print(f"Executed {count} cells: {path}")


if __name__ == "__main__":
    main()
