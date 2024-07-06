from django.db import models

# Create your models here.
class submission(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.IntegerField()

    def __str__(self):
        return self.name