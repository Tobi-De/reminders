#!/command/with-contenv bash

# Restore the database if it does not already exist.
if [ -f /data/db ]; then
	echo "Database already exists, skipping restore"
else
	echo "No database found, restoring from replica if exists"
	exec litestream restore -if-replica-exists -o /data/db "${REPLICA_URL}"
fi

# Migrate the database
cd /app
mkdr /data
python manage.py migrate