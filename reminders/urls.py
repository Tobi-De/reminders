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
        print("Sending test email...")
        send_mail(
            subject="Test email from reminders",
            message="This is a test email.",
            **base_kwargs,
        )


@register_task(
    name="Helmintox",
    schedule_type=Schedule.QUARTERLY,
    next_run=timezone.now().replace(
        year=2024, month=3, day=5, hour=6, minute=0, second=0
    ),
)
def helmintox_reminder():
    print("Sending helmintox reminder...")
    send_mail(
        subject="Buy helmintox",
        message="Go get some helmintox.",
        **base_kwargs,
    )


@register_task(
    name="Difrarel",
    schedule_type=Schedule.MONTHLY,
    next_run=timezone.now().replace(
        year=2024, month=3, day=1, hour=6, minute=0, second=0
    ),
)
def difrarel_reminder():
    print("Sending Difrarel reminder...")
    send_mail(
        subject="Buy some difrarel.",
        message="Go get some difrarel, you eyes my man.",
        **base_kwargs,
    )


@register_task(
    name="Kenny birthday",
    schedule_type=Schedule.YEARLY,
    next_run=timezone.now().replace(
        year=2024, month=2, day=22, hour=6, minute=0, second=0
    ),
)
def kenny_reminder():
    print("Kenny birthday")
    send_mail(
        subject="Kenny birthday",
        message="Lives on the other side of the globe but still one my best friends.",
        **base_kwargs,
    )


@register_task(
    name="Russell birthday",
    schedule_type=Schedule.YEARLY,
    next_run=timezone.now().replace(
        year=2024, month=11, day=9, hour=6, minute=0, second=0
    ),
)
def russell_reminder():
    print("Russell birthday")
    send_mail(
        subject="Russell birthday",
        message="A dumb bitch but my best friend.",
        **base_kwargs,
    )

@register_task(
    name="Gédéon birthday",
    schedule_type=Schedule.YEARLY,
    next_run=timezone.now().replace(
        year=2024, month=6, day=14, hour=6, minute=0, second=0
    ),
)
def gedeon_reminder():
    print("Gédéon birthday")
    send_mail(
        subject="Gédéon birthday",
        message="For some reason, we are close enought that he probably don't care that I wish him a happy birthday.",
        **base_kwargs,
    )

@register_task(
    name="Kossoun birthday",
    schedule_type=Schedule.YEARLY,
    next_run=timezone.now().replace(
        year=2024, month=3, day=8, hour=6, minute=0, second=0
    ),
)
def kossoun_reminder():
    print("Kossoun birthday")
    send_mail(
        subject="Kossoun birthday",
        message="A cousin that I'm close to, that's rare.",
        **base_kwargs,
    )

@register_task(
    name="Kim birthday",
    schedule_type=Schedule.YEARLY,
    next_run=timezone.now().replace(
        year=2024, month=10, day=26, hour=6, minute=0, second=0
    ),
)
def Kim_reminder():
    print("Kim birthday")
    send_mail(
        subject="Kim birthday",
        message="A colleague and a friend",
        **base_kwargs,
    )

@register_task(
    name="Daily journal",
    schedule_type=Schedule.DAILY,
    next_run=timezone.now().replace(
        year=2024, month=2, day=12, hour=21, minute=0, second=0
    ),
)
def journal_reminder():
    print("Daily Journal")
    d = timezone.now().date().strftime("%Y-%m-%d")
    send_mail(
        subject=f"Journal of {d}",
        message=f"Write something - {d} - https://github.com/Tobi-De/second-brain/new/main/Journal/Daily",
        **base_kwargs,
    )


@register_task(
    name="Mohamed birthday",
    schedule_type=Schedule.YEARLY,
    next_run=timezone.now().replace(
        year=2024, month=3, day=20, hour=6, minute=0, second=0
    ),
)
def helm_reminder():
    print("Mohamed Birthday")
    send_mail(
        subject=f"Mohamed Birthday",
        message=f"The only i'm still close to from GLIS",
        **base_kwargs,
    )



