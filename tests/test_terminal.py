import pytest

from khuong.terminal import TerminalCapability, TerminalPolicy, TerminalPolicyError


def test_terminal_executes_allowlisted_command(tmp_path):
    terminal = TerminalCapability(root=tmp_path)
    result = terminal.execute("python -c 'print(2 + 3)'")
    assert result.exit_code == 0
    assert result.stdout.strip() == "5"


def test_terminal_rejects_denied_command(tmp_path):
    terminal = TerminalCapability(root=tmp_path)
    with pytest.raises(TerminalPolicyError):
        terminal.execute("rm -rf x")


def test_terminal_rejects_unknown_command(tmp_path):
    terminal = TerminalCapability(root=tmp_path)
    with pytest.raises(TerminalPolicyError):
        terminal.execute("bash -c 'echo unsafe'")


def test_terminal_cannot_escape_root(tmp_path):
    terminal = TerminalCapability(root=tmp_path)
    with pytest.raises(TerminalPolicyError):
        terminal.execute("pwd", cwd="..")


def test_terminal_timeout(tmp_path):
    terminal = TerminalCapability(root=tmp_path, policy=TerminalPolicy(max_timeout_seconds=0.05))
    result = terminal.execute("python -c 'import time; time.sleep(1)'")
    assert result.timed_out is True
    assert result.exit_code == -1
