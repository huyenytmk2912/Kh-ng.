#!/usr/bin/env python3
"""Khuong environment diagnostic; exits non-zero when required checks fail."""

from __future__ import annotations

import importlib.util
import platform
import shutil
import subprocess
import sys


def command_version(command: str, args: list[str]) -> str | None:
    path = shutil.which(command)
    if not path:
        return None
    try:
        result = subprocess.run(
            [path, *args], capture_output=True, text=True, timeout=10, check=False
        )
    except (OSError, subprocess.TimeoutExpired):
        return None
    output = (result.stdout or result.stderr).strip().splitlines()
    return output[0] if output else None


def main() -> int:
    print(f"python: {sys.version.split()[0]}")
    print(f"platform: {platform.platform()}")
    print(f"executable: {sys.executable}")

    pytest_ok = importlib.util.find_spec("pytest") is not None
    print(f"pytest: {'available' if pytest_ok else 'missing'}")

    cuda_version = command_version("nvidia-smi", ["--query-gpu=driver_version", "--format=csv,noheader"])
    print(f"cuda/nvidia-smi: {cuda_version or 'not detected'}")

    package_ok = importlib.util.find_spec("khuong") is not None
    print(f"khuong-package: {'available' if package_ok else 'missing'}")

    required = {
        "Python >= 3.11": sys.version_info >= (3, 11),
        "pytest": pytest_ok,
        "khuong package": package_ok,
    }
    failed = [name for name, ok in required.items() if not ok]
    if failed:
        print("FAILED:", ", ".join(failed))
        return 1

    print("environment: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
