from django.contrib.auth.models import Permission, User
from django.db import models
from django.core.urlresolvers import reverse


class SignUp (models.Model):
    user_id = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    number = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.user_id


class Complaint(models.Model):
    username = models.CharField(max_length=100)
    email= models.CharField(max_length=100)
    number = models.IntegerField()
    complaint = models.CharField(max_length=500)

    def get_absolute_url(self):
        return reverse('gov1:complaint',kwargs={'pk':self.pk})


    def __str__(self):
        return self.username


class Suggestion(models.Model):
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    number = models.CharField(max_length=100)
    suggestion = models.CharField(max_length=500)

    def __str__(self):
        return self.username


class Birth(models.Model):
    form_no= models.IntegerField()
    date = models.CharField(max_length=100)
    id_number = models.IntegerField()
    name = models.CharField(max_length=100)
    father = models.CharField(max_length=100)
    mother = models.CharField(max_length=100)
    dob = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    occfather = models.CharField(max_length=100)
    occmother = models.CharField(max_length=100)
    birthplace= models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    number = models.IntegerField()
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Water(models.Model):
    form_no = models.CharField(max_length=100)
    cdate = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    fname = models.CharField(max_length=100)
    month = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    amount= models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    connection = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    iproof = models.CharField(max_length=100)
    iproofno= models.CharField(max_length=100)

    def __str__(self):
        return self.form_no


class Voter(models.Model):
    form = models.CharField(max_length=100)
    cdate = models.CharField(max_length=100)
    id_number = models.CharField(max_length=100)
    fname= models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    father = models.CharField(max_length=100)
    month= models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    place= models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.id_number


class Death(models.Model):
    form_no = models.CharField(max_length=100)
    date= models.CharField(max_length=100)
    id_number = models.CharField(max_length=100)
    name= models.CharField(max_length=100)
    father = models.CharField(max_length=100)
    mother= models.CharField(max_length=100)
    dob = models.CharField(max_length=100)
    #dmonth = models.CharField(max_length=100)
    ddate= models.CharField(max_length=100)
    #dyear = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    #deathplace= models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    contact= models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    cause = models.CharField(max_length=100)

    def __str__(self):
        return self.id_number


class Electricity(models.Model):
    form_no = models.CharField(max_length=100)
    cdate = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    fname = models.CharField(max_length=100)
    month = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    amount= models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    connection = models.CharField(max_length=100)
    arra = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    iproof = models.CharField(max_length=100)
    iproofno = models.CharField(max_length=100)

    def __str__(self):
        return self.form_no


class Mobile(models.Model):
    form_no = models.CharField(max_length=100)
    cdate = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    fname = models.CharField(max_length=100)
    month = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    amount = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    connection = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    iproof = models.CharField(max_length=100)
    iproofno = models.CharField(max_length=100)

    def __str__(self):
        return self.form_no


