"""Runtime boundary for model inputs and controlled tool capabilities."""

from __future__ import annotations

from dataclasses import dataclass

from .contracts import ModelMetadata, TokenSequence, validate_compatibility
from .terminal import TerminalCapability, TerminalResult


@dataclass(frozen=True)
class RuntimeConfig:
    context_length: int
    tokenizer_version: str


class RuntimeSession:
    """Validates model/tokenizer inputs and exposes runtime capabilities."""

    def __init__(
        self,
        model: ModelMetadata,
        config: RuntimeConfig,
        *,
        terminal: TerminalCapability | None = None,
    ) -> None:
        model.validate()
        if config.context_length <= 0:
            raise ValueError("context_length must be positive")
        self.model = model
        self.config = config
        self.terminal = terminal

    def validate_input(self, tokens: TokenSequence) -> None:
        validate_compatibility(
            self.model,
            tokens,
            context_length=self.config.context_length,
            tokenizer_version=self.config.tokenizer_version,
        )

    def prepare(self, tokens: TokenSequence) -> tuple[int, ...]:
        self.validate_input(tokens)
        return tokens.ids

    def execute_terminal(
        self,
        command: str | tuple[str, ...],
        *,
        cwd: str | None = None,
        timeout: float | None = None,
    ) -> TerminalResult:
        """Execute a terminal action through the configured capability."""
        if self.terminal is None:
            raise RuntimeError("terminal capability is not configured")
        return self.terminal.execute(command, cwd=cwd, timeout=timeout)
