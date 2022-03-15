from django.db import models

# Create your models here.

class clientuser(models.Model):
    name=models.CharField(default='',max_length=45)
    email=models.EmailField()
    password=models.CharField(default='',max_length=45)
    def __str__(self) -> str:
        return self.name