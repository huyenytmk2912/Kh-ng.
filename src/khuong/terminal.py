"""Policy-controlled terminal capability for direct model tool use."""

from __future__ import annotations

import os
import shlex
import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import Mapping, Sequence


class TerminalPolicyError(PermissionError):
    """Raised when a terminal request violates the configured policy."""


@dataclass(frozen=True)
class TerminalPolicy:
    """Conservative execution policy for model-requested shell commands."""

    allowed_commands: frozenset[str] = frozenset(
        {"cat", "echo", "find", "git", "grep", "ls", "pwd", "python", "pytest", "sed", "wc"}
    )
    denied_commands: frozenset[str] = frozenset(
        {"chmod", "chown", "curl", "dd", "mkfs", "mount", "passwd", "rm", "shutdown", "sudo", "su", "wget"}
    )
    max_timeout_seconds: float = 120.0

    def validate(self, argv: Sequence[str], cwd: Path) -> None:
        if not argv:
            raise TerminalPolicyError("terminal command cannot be empty")
        executable = Path(argv[0]).name
        if executable in self.denied_commands:
            raise TerminalPolicyError(f"command is denied by policy: {executable}")
        if executable not in self.allowed_commands:
            raise TerminalPolicyError(f"command is not allowlisted: {executable}")
        if not cwd.is_dir():
            raise TerminalPolicyError("working directory does not exist")


@dataclass(frozen=True)
class TerminalResult:
    command: tuple[str, ...]
    cwd: str
    stdout: str
    stderr: str
    exit_code: int
    timed_out: bool = False


class TerminalCapability:
    """Execute explicitly allowlisted commands and return observable results."""

    def __init__(self, *, root: str | os.PathLike[str], policy: TerminalPolicy | None = None) -> None:
        self.root = Path(root).resolve()
        self.policy = policy or TerminalPolicy()
        if not self.root.is_dir():
            raise ValueError("terminal root must be an existing directory")

    def _resolve_cwd(self, cwd: str | os.PathLike[str] | None) -> Path:
        candidate = (self.root / (cwd or ".")).resolve()
        if candidate != self.root and self.root not in candidate.parents:
            raise TerminalPolicyError("working directory escapes terminal root")
        return candidate

    def execute(
        self,
        command: str | Sequence[str],
        *,
        cwd: str | os.PathLike[str] | None = None,
        timeout: float | None = None,
        env: Mapping[str, str] | None = None,
    ) -> TerminalResult:
        argv = tuple(shlex.split(command) if isinstance(command, str) else command)
        workdir = self._resolve_cwd(cwd)
        self.policy.validate(argv, workdir)
        limit = self.policy.max_timeout_seconds if timeout is None else min(timeout, self.policy.max_timeout_seconds)
        safe_env = {"PATH": os.environ.get("PATH", "")}
        if env:
            safe_env.update(env)
        try:
            completed = subprocess.run(
                argv,
                cwd=workdir,
                env=safe_env,
                stdin=subprocess.DEVNULL,
                capture_output=True,
                text=True,
                timeout=limit,
                check=False,
            )
            return TerminalResult(argv, str(workdir), completed.stdout, completed.stderr, completed.returncode)
        except subprocess.TimeoutExpired as exc:
            return TerminalResult(
                argv,
                str(workdir),
                (exc.stdout or "") if isinstance(exc.stdout, str) else "",
                (exc.stderr or "") if isinstance(exc.stderr, str) else "",
                -1,
                timed_out=True,
            )
