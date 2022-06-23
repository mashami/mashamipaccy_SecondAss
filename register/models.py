import email
from django import db
from django.db import models

# Create your models here.

class Tranees(models.Model):
    names=models.CharField(max_length=50,null=True,blank=False)
    email=models.CharField(max_length=50,null=True,blank=False)
    userName=models.CharField(max_length=50,null=True,blank=False)
    dob=models.DateField()
    location=models.CharField(max_length=50,null=True,blank=False)

    class Meta():
        db_table="Tranees"

    def __str__(self):
        return f"{self.names}: {self.email}: {self.userName}: {self.dob}: {self.location}"
