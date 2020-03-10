#!/bin/bash

DATE=`date +"%Y-%m-%d_%H-%M-%S"`
DATEFMT='%Y-%m-%d_%H-%M-%S'
DBNAME='chat_db'
DBUSER='chat'
BACKUPPATH='/var/backups'
MAX_BACKUPS=16

echo "Start backup ${DBNAME}"
pg_dump -U $DBUSER -h localhost $DBNAME > $BACKUPPATH/$DATE-${DBNAME}.sql
if [ $? -ne 0 ]
then
	echo "Failed at backup ${DBNAME}"
else
	echo "`date +${DATEFMT}` End backup ${DBNAME}"
	echo "Start remove old backup"
	ls -t $BACKUPPATH/*${DBNAME}.sql | sed -e "1,$(($MAX_BACKUPS))d" | xargs -d '\n' rm
	echo "Done"
fi

