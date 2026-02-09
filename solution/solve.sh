#!/bin/bash
set -e

# This script simulates what the Oracle agent should do
# Install make
apt-get update > /dev/null 2>&1
apt-get install -y make > /dev/null 2>&1

# Run the build
cd /workspace
make all > /dev/null 2>&1

# Verify make is installed
if ! command -v make &> /dev/null; then
    exit 1
fi

# Verify binary exists
if [ ! -f "/workspace/build/app" ]; then
    exit 1
fi

exit 0