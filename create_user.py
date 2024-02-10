from django.conf import settings
from django.contrib.auth.models import User

if not User.objects.filter(username=settings.SUPERUSER_USERNAME).exists():
    print("Creating superuser...")
    User.objects.create_superuser(
        username=settings.SUPERUSER_USERNAME, password=settings.SUPERUSER_PASSWORD
    )
else:
    print("Superuser already exists.")