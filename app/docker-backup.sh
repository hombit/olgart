#!/bin/bash

BACKUP=/backup

while :
do
    sleep 86400
    DIR=$(date '+%y-%m-%d')
    mkdir -p $BACKUP/$DIR
    
    ./manage.py dumpdata > $BACKUP/$DIR/olgart.json
    cp -rv /www/media $BACKUP/$DIR/

    if [ -f $BACKUP/olgart.json ]; then
        mkdir -p $BACKUP/orig
        cp -v $BACKUP/olgart.json $BACKUP/orig/
    fi
    ln -sfv $DIR/olgart.json $BACKUP/
    
    if [ -d $BACKUP/media ]; then
        mkdir -p $BACKUP/orig
        mv -v $BACKUP/media $BACKUP/orig/
    fi
    ln -sfv $DIR/media $BACKUP/
done
