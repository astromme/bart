#!/usr/bin/env bash

DIR="`pwd`"
sed "s|CURRENT_DIR|${DIR}|g" crontab.prototype > crontab
