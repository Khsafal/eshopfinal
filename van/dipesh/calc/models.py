

from django.db import models
from django.contrib.auth.models import User


class file(models.Model):
  file=models.ImageField(upload_to="media")