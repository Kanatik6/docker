from django.db import models


class TestModel(models.Model):
    name = models.CharField(max_length=20)
    value = models.CharField(max_length=30)
    