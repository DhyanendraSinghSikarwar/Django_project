from django.db import models

# Create your models here.
class Member(models.Model):
	firstname = models.CharField(max_length=255)
	lastname = models.CharField(max_length=255)
	phone = models.IntegerField(null=True)
	joined_date = models.DateField(null=True)

  


class Person(models.Model):
  age = models.IntegerField(null=True)
  email= models.CharField(max_length=255)
  address = models.CharField(max_length=255)
  member_id= models.ForeignKey(Member,on_delete=models.CASCADE)

