#!/command/with-contenv sh

alias python="/opt/pysetup/.venv/bin/python"

cd /app

python manage.py migrate
python manage.py shell < create_user.py
python manage.py setup_periodic_tasks