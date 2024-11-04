#!/bin/bash
set -Eeuo pipefail

base_dir=$(dirname $(dirname $0))

# Run the pre-commit checks
echo "Running pre-commit checks..."
pre-commit run --all-files || { echo 'Pre-commit checks failed'; exit 1; }

echo "Running isort..."
isort --sp "${base_dir}/pyproject.toml" --check openfl || { echo 'isort check failed'; exit 1; }

echo "Running black..."
black --config "${base_dir}/pyproject.toml" --check openfl || { echo 'black check failed'; exit 1; }

echo "Running flake8..."
flake8 --config "${base_dir}/setup.cfg" --show-source openfl || { echo 'flake8 check failed'; exit 1; }