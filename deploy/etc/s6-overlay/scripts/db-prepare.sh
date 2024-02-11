#!/command/with-contenv sh

# Restore the database if it does not already exist.
if [ -f /data/db ]; then
	echo "Database already exists, skipping restore"
else
	echo "No database found, restoring from replica if exists"
	exec litestream restore -v -if-replica-exists -o /data/db "${REPLICA_URL}"
fi

cd /app
python manage.py migrate