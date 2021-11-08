#!/bin/bash

set -e

if [ "$EUID" -ne 0 ]; then
    echo "Please run as root"
    exit
fi

NGINX_SITES=/etc/nginx/sites-available

modified=0
for site in $(ls ./nginx); do
    echo "Updating $site..."
    hash_before=$(md5sum $NGINX_SITES/$site)
    cp ./nginx/$site $NGINX_SITES/$site
    [ -f ./updaters/$site.sh ] && echo "Found updater, running it..." && ./updaters/$site.sh $NGINX_SITES/$site
    hash_after=$(md5sum $NGINX_SITES/$site)
    if [ "$hash_before" != "$hash_after" ]; then
        echo "Site $site has been modified, reloading nginx..."
        modified=1
    fi
done

if [ $modified -eq 1 ]; then
    echo "Reloading nginx..."
    systemctl reload nginx
fi
