#!/bin/bash

BACKUP=/backup

while :
do
    sleep 3600
    gdrive --refresh-token $GDRIVETOKEN sync upload --keep-local $BACKUP $GDRIVEDESTINATION
done
