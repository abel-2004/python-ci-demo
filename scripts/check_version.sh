#!/usr/bin/env bash
set -euo pipefail

TAG="${1:?usage: check_version.sh vX.Y.Z}"
VERSION="${TAG#v}"

PY_VERSION=$(python3 -c "import tomllib; print(tomllib.load(open('pyproject.toml', 'rb'))['project']['version'])")
NPM_VERSION=$(node -p "require('./npm/package.json').version")

[ "$PY_VERSION" = "$VERSION" ] || { echo "FAIL pyproject.toml is $PY_VERSION, tag is $VERSION"; exit 1; }
[ "$NPM_VERSION" = "$VERSION" ] || { echo "FAIL npm/package.json is $NPM_VERSION, tag is $VERSION"; exit 1; }

echo "OK: all versions match $VERSION"
