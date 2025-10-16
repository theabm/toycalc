# tests/test_cli.py
import subprocess
import sys

import pytest

from toycalc.cli import main


def run_main(argv, capsys):
    # helper to run main() with custom argv and capture output
    old_argv = sys.argv[:]
    try:
        sys.argv = ["toycalc", *argv]
        main()
        return capsys.readouterr()
    finally:
        sys.argv = old_argv


def test_cli_add(capsys):
    out = run_main(["add", "2", "3"], capsys)
    assert out.out.strip() == "5"


@pytest.mark.parametrize("n, val", [(0, "0"), (1, "1"), (5, "5"), (10, "55")])
def test_cli_fib(capsys, n, val):
    out = run_main(["fib", str(n)], capsys)
    assert out.out.strip() == val


def test_cli_fib_negative_raises():
    # core.fib raises ValueError; allow it to bubble up
    with pytest.raises(ValueError):
        main_argv = ["toycalc", "fib", "-1"]
        sys.argv = main_argv
        try:
            main()
        finally:
            # ensure argv restored even on exception
            sys.argv = ["pytest"]


def test_cli_help_exits_with_usage(capsys):
    # argparse prints help then exits(0)
    with pytest.raises(SystemExit) as e:
        sys.argv = ["toycalc", "-h"]
        try:
            main()
        finally:
            sys.argv = ["pytest"]
    assert e.value.code == 0
    out = capsys.readouterr()
    assert "usage:" in out.out.lower()


def test_cli_missing_args_exits_with_error(capsys):
    # no subcommand -> argparse error -> exit(2) + usage on stderr
    with pytest.raises(SystemExit) as e:
        sys.argv = ["toycalc"]
        try:
            main()
        finally:
            sys.argv = ["pytest"]
    assert e.value.code == 2
    err = capsys.readouterr().err.lower()
    assert "usage:" in err or "the following arguments are required" in err


def test_entry_point_via_module():
    # optional: verify console entry via `python -m toycalc.cli`
    completed = subprocess.run(
        [sys.executable, "-m", "toycalc.cli", "add", "2", "3"],
        check=True,
        capture_output=True,
        text=True,
    )
    assert completed.stdout.strip() == "5"
