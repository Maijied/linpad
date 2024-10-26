#!/bin/bash

# Read the current version from snapcraft.yaml
CURRENT_VERSION=$(grep -Po '(?<=^version: ")([0-9]+\.[0-9]+\.[0-9]+)(?=")' snapcraft.yaml)

# Split the version into an array
IFS='.' read -r -a VERSION_PARTS <<< "$CURRENT_VERSION"

# Increment the last part of the version
LAST_PART_INDEX=$((${#VERSION_PARTS[@]} - 1))
VERSION_PARTS[$LAST_PART_INDEX]=$((${VERSION_PARTS[$LAST_PART_INDEX]} + 1))

# Join the version parts back into a string
NEW_VERSION=$(IFS=.; echo "${VERSION_PARTS[*]}")

# Update the version in snapcraft.yaml
sed -i "s/^version: .*/version: \"$NEW_VERSION\"/" snapcraft.yaml

echo "Updated version to $NEW_VERSION"

# Build the Snap
snapcraft

# Test the Snap Locally
sudo snap install linpad_*.snap --dangerous
linpad

# Login to Snapcraft (if not already logged in)
snapcraft login

# Push the Snap to the Snap Store
snapcraft upload linpad_*.snap --release stable

# Check the Status
snapcraft status linpad