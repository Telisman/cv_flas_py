from django.db import models

class Info(models.Model):
    name = models.CharField(max_length=15, default= None)
    last_name = models.CharField(max_length=15, default= None)
    date_of_birth = models.DateField()
    address = models.CharField(max_length=30)
    email = models.EmailField()
    phone_number = models.IntegerField()
    def __str__(self):
        return 'Info: {} || {} || {} || {} || {}'.format(self.name, self.last_name, self.date_of_birth, self.address, self.email)

class WorkExperience(models.Model):
    start_date = models.DateField()
    end_date = models.DateField(auto_now_add= False,auto_now=False,blank=True,null=True)
    company = models.CharField(max_length=30)
    position = models.CharField(max_length=30)
    description = models.TextField()
    address  = models.CharField(max_length=40,blank=True)
    def __str__(self):
        return 'Work: {} || {}'.format(self.company, self.position)


class Education(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    school = models.CharField(max_length=30)
    section = models.CharField(max_length=80)
    def __str__(self):
        return 'Education: {} || {} || {}'.format(self.school, self.start_date, self.end_date)



class Portfolio(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()

    def __str__(self):
        return 'Portfolio: {} || {}'.format(self.title, self.description)

