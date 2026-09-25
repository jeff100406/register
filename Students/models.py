from django.db import models

class admission(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    course = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    address = models.TextField()

    def __str__(self):
        return self.name
