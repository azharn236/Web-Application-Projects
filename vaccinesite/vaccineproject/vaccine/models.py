from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=250, unique=True)
    gender = models.CharField(max_length=50)
    age = models.IntegerField()
    date_of_birth = models.DateField()
    mobile_no = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'person'

    def __str__(self):
        return '{}'. format(self.name)
