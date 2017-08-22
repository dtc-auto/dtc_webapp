from __future__ import unicode_literals  # don't know if necessary
from django.db import models

KIND_CHOICES = (
    ('tech', 'tech'),
    ('dbtech', 'dbtech'),
    ('economics', 'economics')
)


# Create your models here.
class Moment(models.Model):
    content = models.CharField(max_length=200)
    user_name = models.CharField(max_length=20, default='anonymous')
    kind = models.CharField(max_length=20, choices=KIND_CHOICES, default=KIND_CHOICES[0])
