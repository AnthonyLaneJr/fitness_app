from django.contrib import admin
from .models import AgeGroup, FitnessUser, Gender
# Register your models here.

admin.site.register(AgeGroup)
admin.site.register(FitnessUser)
admin.site.register(Gender)
