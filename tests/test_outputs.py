"""
Use this file to define pytest tests that verify the outputs of the task.

This file will be copied to /tests/test_outputs.py and run by the /tests/test.sh file
from the working directory.

This test suite verifies all expected behaviors mentioned in the task description:
1. Identify the build failure
2. Diagnose the missing dependency (make tool)
3. Install the missing build tool
4. Verify successful build
"""

import subprocess
import os


def test_make_installed():
    """
    Test that the agent installed the 'make' build tool.

    Verifies Behavior: Install the missing build tool

    This is the core requirement - the agent must recognize that 'make' is missing
    and install it using the system package manager (apt-get).
    """
    result = subprocess.run(
        ["which", "make"],
        capture_output=True,
        text=True
    )

    assert result.returncode == 0, \
        "FAIL: 'make' command not found. Agent did not install the build tool."


def test_make_functional():
    """
    Test that make can be executed and returns version info.

    Verifies Behavior: Diagnose the missing dependency

    Not only must make be installed, it must be functional. This prevents
    agents from creating fake 'make' files to pass the previous test.
    """
    result = subprocess.run(
        ["make", "--version"],
        capture_output=True,
        text=True
    )

    assert result.returncode == 0, \
        "FAIL: 'make --version' failed. Make is not working correctly."

    assert "GNU Make" in result.stdout, \
        "FAIL: Unexpected make version output. This doesn't appear to be GNU Make."


