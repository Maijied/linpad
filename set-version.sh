#!/bin/bash
VERSION="1.0.1-$(git rev-parse --short HEAD)"
sed -i "s/^version: .*/version: \"$VERSION\"/" snapcraft.yaml