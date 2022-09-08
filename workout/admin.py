from django.contrib import admin
from .models import SingleWorkout, Workout_template, Week
# Register your models here.

admin.site.register(SingleWorkout)
admin.site.register(Week)
admin.site.register(Workout_template)