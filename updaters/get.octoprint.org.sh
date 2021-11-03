#!/bin/bash

set -e

source ../helpers.sh

CONFIG="$1"

REPO="OctoPrint/OctoPrint"
URL="https://api.github.com/repos/$REPO/releases"
DATA=$(curl --silent "$URL")

stable=$(echo $DATA | jq -r '[ .[] | select(.prerelease != true) ][0].tag_name')
stable_index=$(echo $DATA | jq -r 'map(.prerelease != true) | index(true)')
stable_major_minor=$(echo $stable | awk -F "." '{print $1 "." $2}')
last=$(echo $DATA | jq -r "[ .[] | select(.prerelease != true and (.tag_name | startswith(\"$stable_major_minor.\") | not)) ][0].tag_name")

if [ $stable_index -ne 0 ]; then
    maintenance=$(echo $DATA | jq -r ".[0:$stable_index] | [ .[] | select(.prerelease and .target_commitish == \"rc/maintenance\") ][0].tag_name")
    devel=$(echo $DATA | jq -r ".[0:$stable_index] | [ .[] | select(.prerelease and (.target_commitish == \"rc/maintenance\" or .target_commitish == \"rc/devel\")) ][0].tag_name")
else
    maintenance=$stable
    devel=$stable
fi

echo "Stable: $stable (index: $stable_index, major.minor: $stable_major_minor)"
echo "Maintenance: $maintenance"
echo "Devel: $devel"
echo "Last: $last"

current_stable=$(get_nginx_var "stable" "$CONFIG")
current_maintenance=$(get_nginx_var "maintenance" "$CONFIG")
current_devel=$(get_nginx_var "devel" "$CONFIG")
current_last=$(get_nginx_var "last" "$CONFIG")

echo "Current stable: $current_stable"
echo "Current maintenance: $current_maintenance"
echo "Current devel: $current_devel"
echo "Current last: $current_last"

if [[ "$stable" != "$current_stable" ]]; then
    echo "Setting stable to $stable..."
    set_nginx_var "stable" "$stable" $CONFIG
fi
if [[ "$maintenance" != "$current_maintenance" ]]; then
    echo "Setting maintenance to $maintenance..."
    set_nginx_var "maintenance" "$maintenance" $CONFIG
fi
if [[ "$devel" != "$current_devel" ]]; then
    echo "Setting devel to $devel..."
    set_nginx_var "devel" "$devel" $CONFIG
fi
if [[ "$last" != "$current_last" ]]; then
    echo "Setting last to $last..."
    set_nginx_var "last" "$last" $CONFIG
fi
