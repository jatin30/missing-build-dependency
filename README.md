# Missing Make Dependency - Terminal Bench Task

## Overview

This task tests an AI agent's ability to diagnose and fix a build failure caused by a missing system-level build tool (`make`).

## Category

**Missing Build Dependencies** - Installing missing compilers or system libraries required for builds

---

## Task Structure

```
missing-make-dependency/
├── task.toml                          # Task configuration
├── instruction.md                     # Instructions for the AI agent
├── README.md                          # This file
├── environment/
│   ├── Dockerfile                     # Environment setup (NO make installed)
│   └── project_files/
│       ├── Makefile                   # Build instructions
│       ├── build.sh                   # Build script (will fail)
│       └── src/
│           └── main.c                 # Simple C application
├── solution/
│   └── solve.sh                       # Solution script (installs make & builds)
└── tests/
    ├── test.sh                        # Test runner (Harbor format)
    └── test_outputs.py                # Pytest test case
```

---

## How It Works

### Initial State (Broken)
1. Docker container has `gcc` compiler but NOT `make`
2. When build script runs, it fails with: **"make: command not found"**
3. Build cannot complete without `make`

### What the Agent Must Do
1. **Identify** the build failure
2. **Diagnose** that `make` is missing from the error message
3. **Install** make using: `apt-get install -y make`
4. **Verify** the build succeeds

### Success Criteria
✅ The file `/workspace/build/app` exists (built binary)  
✅ `make` command is available in the system

---

## File Descriptions

### task.toml
Task configuration file with:
- Task metadata (name, category, difficulty)
- Environment settings (Docker, Python 3.12)
- Evaluation configuration (points to solution/solve.sh)
- Timeout settings (300 seconds)

### instruction.md
Human-readable task description that the AI agent reads. Contains:
- Problem statement
- Expected behaviors
- Success criteria
- Hints and constraints

### environment/Dockerfile
Sets up the container environment:
- Base: Ubuntu 22.04
- Installs: gcc, libc6-dev (NOT make - that's the problem!)
- Copies: Makefile, build.sh, main.c
- Working directory: /workspace

### environment/project_files/
**Makefile**: Standard make build file that compiles main.c  
**build.sh**: Shell script that runs `make all`  
**src/main.c**: Simple C program that prints "Hello from the built application!"

### solution/solve.sh
The solution script that:
1. Installs make via apt-get
2. Runs the build process
3. Verifies success
4. Returns exit code 0 on success, 1 on failure

### tests/test.sh
Harbor's standard test runner that:
- Installs UV and pytest
- Runs test_outputs.py
- Generates CTRF JSON report
- Writes reward (0 or 1) to /logs/verifier/reward.txt

### tests/test_outputs.py
Pytest test case that verifies:
- `make` command is installed and available

---


## Testing Instructions

### Prerequisites

1. **Install UV**:
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. **Install Harbor**:
   ```bash
   uv tool install harbor
   ```

3. **Verify Installation**:
   ```bash
   harbor --version
   ```

### Sanity Tests (Required Before Submission)

Navigate to your task directory:
```bash
cd /path/to/missing-make-dependency
```

**Test 1: NOP Agent (Must Fail ❌)**
```bash
harbor run -p . -a nop
```
**Expected Result**: 
- Status: FAILED
- Reward: 0.0
- Reason: NOP does nothing, so make is never installed

**Test 2: Oracle Agent (Must Pass ✅)**
```bash
harbor run -p . -a oracle
```
**Expected Result**:
- Status: PASSED
- Reward: 1.0
- Reason: Oracle runs solve.sh which installs make and builds successfully

### Interpreting Results

✅ **CORRECT** - If:
- NOP reward = 0.0 (fails)
- Oracle reward = 1.0 (passes)

❌ **INCORRECT** - If:
- NOP reward = 1.0 (shouldn't pass!)
- Oracle reward = 0.0 (shouldn't fail!)

---

## Solution Walkthrough

What the Oracle agent does (via solve.sh):

bash
# 1. Update package lists
apt-get update

# 2. Install make
apt-get install -y make

# 3. Navigate to workspace
cd /workspace

# 4. Run the build
make all
# Output: Compiling application... Build completed successfully!

# 5. Verify binary exists
ls -la /workspace/build/app

# 6. Test the application
./build/app
# Output: Hello from the built application!

## Troubleshooting

### Issue: Harbor not found
```bash
# Add to PATH
export PATH="$HOME/.local/bin:$PATH"
# Or restart terminal
```

### Issue: NOP passes (should fail!)
- Check Dockerfile - did you accidentally install make?
- Look for `make` or `build-essential` in apt-get install
- Dockerfile should ONLY have gcc and libc6-dev

### Issue: Oracle fails (should pass!)
- Check solve.sh is executable: `ls -la solution/solve.sh`
- Make it executable: `chmod +x solution/solve.sh`
- Check test.sh is executable: `chmod +x tests/test.sh`
- Verify all project files exist in environment/project_files/

### Issue: Docker build fails
- Ensure all files in environment/project_files/ exist
- Check Dockerfile syntax
- Verify COPY paths are correct


## Quick Reference

| Command | Expected Result |
|---------|-----------------|
| `harbor run -p . -a nop` | Reward: 0.0 (FAIL) |
| `harbor run -p . -a oracle` | Reward: 1.0 (PASS) |

---
