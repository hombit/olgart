#!/usr/bin/env python

import os
import shutil
import sys



BACKUP = '/backup'
FILES = '/local_backup/files'

if '--force' in sys.argv or '-f' in sys.argv:
    for f in os.listdir(BACKUP):
        path = os.path.join(BACKUP, f)
        shutil.rmtree(path)
    print('Old backups have been deleted')

if not os.path.exists(BACKUP) or len(os.listdir(BACKUP)) == 0:
    for f in os.listdir(FILES):
        path_from = os.path.join(FILES, f)
        path_to = os.path.join(BACKUP, f)
        if os.path.isdir(path_from):
            shutil.copytree(path_from, path_to)
        else:
            shutil.copy(path_from, path_to)
    print('Backup files are copied to {}'.format(BACKUP))
else:
    print("Backup files haven't been copied")

