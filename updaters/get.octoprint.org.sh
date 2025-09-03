#!/bin/bash

set -e

CONFIG="$1"
SCRIPT_DIR=$(cd $(dirname "${BASH_SOURCE[0]}") && pwd)

source "$SCRIPT_DIR/../helpers.sh"

REPO="OctoPrint/OctoPrint"
URL="https://api.github.com/repos/$REPO/releases"
DATA=$(curl --silent "$URL")

stable=$(echo $DATA | jq -r '[ .[] | select(.prerelease != true) ][0].tag_name')
stable_index=$(echo $DATA | jq -r 'map(.prerelease != true) | index(true)')
stable_major_minor=$(echo $stable | awk -F "." '{print $1 "." $2}')
last=$(echo $DATA | jq -r "[ .[] | select(.prerelease != true and (.tag_name | startswith(\"$stable_major_minor.\") | not)) ][0].tag_name")

if [ $stable_index -ne 0 ]; then
    next=$(echo $DATA | jq -r ".[0:$stable_index] | [ .[] | select(.prerelease and (.target_commitish == \"next\" or .target_commitish == \"rc/maintenance\" or .target_commitish == \"rc/devel\")) ][0].tag_name")
else
    next=$stable
fi

echo "Stable: $stable (index: $stable_index, major.minor: $stable_major_minor)"
echo "Next: $next"
echo "Last: $last"

current_stable=$(get_nginx_var "stable" "$CONFIG")
current_next=$(get_nginx_var "next" "$CONFIG")
current_last=$(get_nginx_var "last" "$CONFIG")

echo "Current stable: $current_stable"
echo "Current next: $current_next"
echo "Current last: $current_last"

if [[ "$stable" != "$current_stable" ]]; then
    echo "Setting stable to $stable..."
    set_nginx_var "stable" "$stable" $CONFIG
fi
if [[ "$next" != "$current_next" ]]; then
    echo "Setting next to $next..."
    set_nginx_var "next" "$next" $CONFIG
fi
if [[ "$last" != "$current_last" ]]; then
    echo "Setting last to $last..."
    set_nginx_var "last" "$last" $CONFIG
fi
