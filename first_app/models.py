from django.db import models

# Create your models here.


class Students(models.Model):
    first_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    mobile = models.IntegerField()
    address = models.CharField(max_length=50)
    class_name = models.IntegerField(default=5)

    def __str__(self):
        return self.first_name
