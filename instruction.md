# Missing Make Build Tool - Fix Build Failure

## Problem Statement

A software project needs to be built, but the build process is failing with an error indicating that a required build tool is missing from the system.

## Your Task

Your goal is to diagnose why the build is failing and fix the issue so that the project builds successfully.

## Background

Many software projects use build automation tools to compile code, manage dependencies, and create executable binaries. The most common build tool on Unix/Linux systems is `make`, which reads instructions from a `Makefile` to execute build steps.

## Expected Behaviors to Demonstrate

1. **Identify the build failure**: Attempt to run the build and observe the failure
2. **Diagnose the missing dependency**: Recognize that a required build tool is not installed on the system
3. **Install the missing build tool**: Install the necessary system package to provide the build tool
4. **Verify successful build**: Re-run the build process and confirm it completes successfully

## Success Criteria

The task is complete when the following file exists:

/workspace/build/app


## Files Present

- `/workspace/Makefile`: Build instructions for the project
- `/workspace/src/main.c`: Simple C source code file
- `/workspace/build.sh`: Shell script that initiates the build process

## Starting Point

Run the build script to see the failure:
```bash
cd /workspace
./build.sh
```

## Constraints

- You must use the system package manager to install required tools
- You cannot modify the Makefile or source code
- You cannot create workarounds or mock the build process
- The solution must address the root cause (missing build tool)

## Hints

- Read the error message carefully - it will tell you exactly what's missing
- The missing tool is a standard build utility available in the default package repositories
- After installing the tool, you'll need to re-run the build script
