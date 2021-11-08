#!/bin/bash

set -e

if [ "$EUID" -ne 0 ]; then
    echo "Please run as root"
    exit
fi

NGINX_SITES=/etc/nginx/sites-available

modified=0
for updater in $(ls ./updaters); do
    site=$(basename $updater .sh)
    config="$NGINX_SITES/$site"
    if [ -f "$config" ]; then
        echo "Running updater $updater..."
        hash_before=$(md5sum "$config")
        ./updaters/$updater "$config"
        hash_after=$(md5sum "$config")
        if [ "$hash_before" != "$hash_after" ]; then
            echo "Updater $updater modified $config"
            modified=1
        fi
    fi
done

if [ $modified -eq 1 ]; then
    echo "Reloading nginx..."
    systemctl reload nginx
fi
