#!/bin/bash

set -e

if [ "$EUID" -ne 0 ]; then
    echo "Please run as root"
    exit
fi

NGINX_SITES=/etc/nginx/sites-available

for site in $(ls ./nginx); do
    echo "Updating $site..."
    cp ./nginx/$site $NGINX_SITES/$site
    [ -f ./updaters/$site.sh ] && echo "Found updater, running it..." && ./updaters/$site.sh
done

systemctl reload nginx
