"""Provider-neutral tool calling protocol.

The model should emit structured tool calls; execution remains outside the
model so permissions and sandboxing can be enforced by the host runtime.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Protocol


@dataclass(frozen=True)
class ToolCall:
    name: str
    arguments: dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class ToolResult:
    ok: bool
    output: str
    error: str | None = None


class Tool(Protocol):
    name: str
    description: str

    def execute(self, arguments: dict[str, Any]) -> ToolResult:
        ...
