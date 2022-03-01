#!/bin/bash

set -e

CONFIG="$1"
SCRIPT_DIR=$(cd $(dirname "${BASH_SOURCE[0]}") && pwd)

source "$SCRIPT_DIR/../helpers.sh"

DATA_FILE="$SCRIPT_DIR/../data/faq.octoprint.org/mapping.json"

ENTRIES=$(cat $DATA_FILE | jq -r "to_entries | map(\"\tlocation /\" + .key + \" {\n\t\texpires 0d;\n\t\tadd_header Cache-Control \\\"no-cache\\\";\n\t\treturn 302 \" + .value + \";\n\t}\n\") | join(\"\n\")")

prefix=$(sed '/# managed by updater/q' "$CONFIG")
suffix=$(sed '/# \/ managed by updater/,$!d' "$CONFIG")

echo "$prefix" > "$CONFIG"
echo "$ENTRIES" >> "$CONFIG"
echo "$suffix" >> "$CONFIG"
