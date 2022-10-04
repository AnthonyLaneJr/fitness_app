from django.contrib import admin
from .models import AgeGroup, FitnessUser, Gender
from workout.models import Workout_template
# Register your models here.

admin.site.register(AgeGroup)
admin.site.register(FitnessUser)
admin.site.register(Gender)
