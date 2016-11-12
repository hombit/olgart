#!/usr/bin/env python3

import psycopg2
from time import sleep

while True:
    try:
        conn = psycopg2.connect("host=db user=olgart dbname=olgart")
        conn.close();
        break
    except:
        sleep(0.1)
        pass
