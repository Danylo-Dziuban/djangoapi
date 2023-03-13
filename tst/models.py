from django.db import models


class Tst(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    email = models.CharField(max_length=400)

    def __str__(self):
        return self.name
