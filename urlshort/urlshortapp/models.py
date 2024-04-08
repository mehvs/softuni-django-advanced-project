from django.db import models
from django.contrib.auth.models import AbstractUser
import string
import random


def generate_short_code():
    characters = string.ascii_letters + string.digits
    short_code = ''.join(random.choice(characters) for _ in range(6))
    return short_code


# Create your models here.

class User(AbstractUser):
    pass


class Url(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    original_url = models.URLField()
    short_code = models.CharField(max_length=10, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.short_code = generate_short_code()
        return super().save(*args, **kwargs)


class ClickStats(models.Model):
    url = models.ForeignKey(Url, on_delete=models.CASCADE)
    click_time = models.DateTimeField(auto_now_add=True)
    country_code = models.CharField(max_length=3, blank=True, null=True)
    user_agent = models.TextField(blank=True, null=True)
    click_count = models.IntegerField(default=0, blank=False, null=False)
