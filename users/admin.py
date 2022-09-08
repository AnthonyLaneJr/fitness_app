from django.contrib import admin
from .models import AgeGroup, FitnessUser, UserList, Frequency, Gender, Goal
# Register your models here.

admin.site.register(AgeGroup)
admin.site.register(FitnessUser)
admin.site.register(UserList)
admin.site.register(Frequency)
admin.site.register(Gender)
admin.site.register(Goal)
