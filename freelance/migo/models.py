from distutils.command.upload import upload
from tkinter import CASCADE
from turtle import title
from django.db import models

# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length= 20)
    address = models.TextField()
    def __str__(self):
        return self.name

class Participant(models.Model):
    participant = models.EmailField()
    def __str__(self):
        return self.participant

class Meetups(models.Model):
    title = models.CharField(max_length=20)
    organizer_email = models.EmailField()
    date = models.DateField()
    description = models.TextField()
    image = models.ImageField(upload_to='images')
    location = models.ForeignKey(Location, on_delete= models.CASCADE)
    participant = models.ForeignKey(Participant, on_delete = models.CASCADE)
    def __str__(self):
        return self.title