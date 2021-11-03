#!/bin/bash

set -e

if [ "$EUID" -ne 0 ]; then
    echo "Please run as root"
    exit
fi

NGINX_SITES=/etc/nginx/sites-available

for updater in $(ls ./updaters); do
    site=$(basename $updater .sh)
    [ -f "$NGINX_SITES/$site" ] && echo "Running updater $updater..." && ./updaters/$updater $NGINX_SITES/$site
done

systemctl reload nginx
