from django.db import models


# Create your models here.
class EventDetails(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True)
    date = models.DateTimeField()
    medium = models.CharField(max_length=200)


class ParticipantDetails(models.Model):
    name = models.CharField(max_length=200)
    contact = models.CharField(max_length=200)


class AudienceDetails(models.Model):
    name = models.CharField(max_length=200)
    contact = models.CharField(max_length=200)


class RegistrationForm(models.Model):
    registration_date = models.DateTimeField(auto_now=True)
    event = models.OneToOneField(EventDetails, on_delete=models.CASCADE)
    audience = models.OneToOneField(AudienceDetails, on_delete=models.CASCADE)
    participant = models.OneToOneField(ParticipantDetails, on_delete=models.CASCADE)
