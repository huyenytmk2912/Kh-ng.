import pytest

from khuong.contracts import ModelMetadata
from khuong.runtime import RuntimeConfig, RuntimeSession
from khuong.terminal import TerminalCapability


def make_model() -> ModelMetadata:
    return ModelMetadata(
        model_name="khuong-test",
        model_version="0.1.0",
        tokenizer_version="tok-0.1",
        vocab_size=128,
        context_length=128,
    )


def test_runtime_can_execute_terminal_without_agent(tmp_path):
    runtime = RuntimeSession(
        make_model(),
        RuntimeConfig(context_length=128, tokenizer_version="tok-0.1"),
        terminal=TerminalCapability(root=tmp_path),
    )
    result = runtime.execute_terminal("python -c 'print(7 * 6)'")
    assert result.exit_code == 0
    assert result.stdout.strip() == "42"


def test_runtime_requires_terminal_capability(tmp_path):
    runtime = RuntimeSession(
        make_model(),
        RuntimeConfig(context_length=128, tokenizer_version="tok-0.1"),
    )
    with pytest.raises(RuntimeError, match="terminal capability is not configured"):
        runtime.execute_terminal("pwd")
