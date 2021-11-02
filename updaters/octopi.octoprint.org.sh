#!/bin/bash

set -e

if [ "$EUID" -ne 0 ]; then
    echo "Please run as root"
    exit
fi

REPO="OctoPrint/OctoPi-UpToDate"
URL="https://api.github.com/repos/$REPO/releases"
CONFIG="/etc/nginx/sites-available/octopi.octoprint.org"
DATA=$(curl --silent "$URL")

latest=$(echo $DATA | jq -r '[ .[] | select(.prerelease != true) ][0].assets | [ .[] | select(.content_type == "application/zip") ] | .[0].browser_download_url')
next=$(echo $DATA | jq -r '.[0] | select(.prerelease) | .assets | [ .[] | select(.content_type == "application/zip") ] | .[0].browser_download_url')
current_latest=$(grep 'set $latest_image' "$CONFIG" | awk -F " " '{$1=$3;gsub(/"/, "", $1);print substr($1, 1, length($1) - 1)}')
current_next=$(grep 'set $next_image' "$CONFIG" | awk -F " " '{$1=$3;gsub(/"/, "", $1);print substr($1, 1, length($1) - 1)}')

[ -z "$next" ] && next=$latest

echo "Latest: $latest"
echo "Next: $next"
echo "Current latest: $current_latest"
echo "Current next: $current_next"

if [[ "$latest" != "$current_latest" ]]; then
    echo "Setting latest_image to $latest..."
    sed -i "s@set \$latest_image .*@set \$latest_image \"$latest\";@g" "$CONFIG"
fi
if [[ "$next" != "$current_next" ]]; then
    echo "Setting next_image to $next..."
    sed -i "s@set \$next_image .*@set \$next_image \"$next\";@g" "$CONFIG"
fi
