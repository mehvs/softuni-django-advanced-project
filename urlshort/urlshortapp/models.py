from django.db import models
from django.contrib.auth.models import AbstractUser
import string
import random


def generate_short_code():
    characters = string.ascii_letters + string.digits
    short_code = ''.join(random.choice(characters) for _ in range(6))
    return short_code


REASON_CHOICES = (
    ("spam", "Spam"),
    ("phishing", "Phishing"),
    ("scam", "Scam"),
    ("malicious", "Malicious"),
    ("other", "Other"),
)

STATUS_CHOICES = (
    ("open", "Open"),
    ("pending", "Pending"),
    ("resolved", "Resolved"),
    ("closed", "Closed"),
)


# Create your models here.

class User(AbstractUser):
    pass


class Url(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    original_url = models.URLField()
    short_code = models.CharField(max_length=10, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    click_count = models.PositiveIntegerField(default=0, blank=False, null=False)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.short_code = generate_short_code()
        return super().save(*args, **kwargs)


class ClickStats(models.Model):
    url = models.ForeignKey(Url, on_delete=models.CASCADE)
    click_time = models.DateTimeField(auto_now_add=True)
    country_code = models.CharField(max_length=3, blank=True, null=True)
    user_agent = models.TextField(blank=True, null=True)


class Report(models.Model):
    date_of_report = models.DateTimeField(auto_now_add=True)
    suspected_link = models.URLField()
    reason = models.CharField(blank=False, null=False, choices=REASON_CHOICES, max_length=20)
    additional_notes = models.TextField(blank=True, null=True)
    status = models.CharField(blank=False, null=False, default='Open', choices=STATUS_CHOICES, max_length=20)


class Support(models.Model):
    subject = models.CharField(max_length=255, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    status = models.CharField(blank=False, null=False, default='Open', choices=STATUS_CHOICES, max_length=20)
