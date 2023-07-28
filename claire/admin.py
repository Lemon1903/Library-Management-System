from django.contrib import admin

from .models import AudienceDetails, EventDetails, ParticipantDetails, RegistrationForm

# Register your models here.
admin.site.register(AudienceDetails)
admin.site.register(EventDetails)
admin.site.register(ParticipantDetails)
admin.site.register(RegistrationForm)
