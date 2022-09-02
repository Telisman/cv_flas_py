from django.db import models

class Info(models.Model):
    name = models.CharField(max_length=15, default= None)
    last_name = models.CharField(max_length=15, default= None)
    date_of_birth = models.DateField()
    address = models.CharField(max_length=15)
    email = models.EmailField()
    phone_number = models.IntegerField()


class WorkExperience(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    company = models.CharField(max_length=15)
    position = models.CharField(max_length=25)
    description = models.TextField()

class Education(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    school = models.CharField(max_length=15)

class Portfolio(models.Model):
    title = models.CharField(max_length=15)
    description = models.TextField()




