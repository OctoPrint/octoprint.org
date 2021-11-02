#!/bin/bash

set -e

if [ "$EUID" -ne 0 ]; then
    echo "Please run as root"
    exit
fi

for updater in $(ls ./updaters); do
    echo "Running updater $updater..."
    ./updaters/$updater
done

systemctl reload nginx
