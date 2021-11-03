#!/bin/bash

set -e

source ../helpers.sh

CONFIG="$1"

REPO="OctoPrint/OctoPi-UpToDate"
URL="https://api.github.com/repos/$REPO/releases"
DATA=$(curl --silent "$URL")

latest=$(echo $DATA | jq -r '[ .[] | select(.prerelease != true) ][0].assets | [ .[] | select(.content_type == "application/zip") ] | .[0].browser_download_url')
next=$(echo $DATA | jq -r '.[0] | select(.prerelease) | .assets | [ .[] | select(.content_type == "application/zip") ] | .[0].browser_download_url')
[ -z "$next" ] && next=$latest

echo "Latest: $latest"
echo "Next: $next"

current_latest=$(get_nginx_var "latest_image" "$CONFIG")
current_next=$(get_nginx_var "next_image" "$CONFIG")

echo "Current latest: $current_latest"
echo "Current next: $current_next"

if [[ "$latest" != "$current_latest" ]]; then
    echo "Setting latest_image to $latest..."
    set_nginx_var "latest_image" "$latest" "$CONFIG"
fi
if [[ "$next" != "$current_next" ]]; then
    echo "Setting next_image to $next..."
    set_nginx_var "next_image" "$next" "$CONFIG"
fi
