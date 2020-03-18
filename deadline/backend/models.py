from django.db import models


class User(models.Model):
  first = models.CharField(max_length=200)
  last = models.CharField(max_length=200)
  password = models.CharField(max_length=200)
  email = models.CharField(max_length=200)
  role = models.CharField(max_length=200)