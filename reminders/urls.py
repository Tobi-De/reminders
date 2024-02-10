from contextlib import suppress

from django.conf import settings
from django.contrib import admin
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.db.utils import OperationalError
from django.urls import path
from django.utils import timezone
from django_q.models import Schedule
from django_q_registry import register_task

urlpatterns = [path("", admin.site.urls)]

base_kwargs = {
    "from_email": "noreply@oluwatobi.dev",
    "recipient_list": ["tobidegnon@proton.me"],
}


@register_task(
    name="Send periodic test email",
    schedule_type=Schedule.MINUTES,
    minutes=5,
    next_run=timezone.now(),
)
def send_test_email():
    if settings.TEST_EMAIL_ENABLED:
        send_mail(
            subject="Test email from reminders",
            message="This is a test email.",
            **base_kwargs,
        )


@register_task(
    name="Helmintox",
    schedule_type=Schedule.MONTHLY,
    next_run=timezone.datetime(2024, 3, 5, 6, 0, 0),
)
def helmintox_reminder():
    send_mail(
        subject="Buy helmintox",
        message="Go get some helmintox.",
        **base_kwargs,
    )


with suppress(OperationalError):
    if not User.objects.filter(username=settings.SUPERUSER_USERNAME).exists():
        User.objects.create_superuser(
            username=settings.SUPERUSER_USERNAME, password=settings.SUPERUSER_PASSWORD
        )
