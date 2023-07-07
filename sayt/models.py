from django.db import models

# Create your models here.


class Subscribe(models.Model):
    email = models.CharField(max_length=128)

    def __str__(self):
        return self.email