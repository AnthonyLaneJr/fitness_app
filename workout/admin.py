from django.contrib import admin
from .models import Workout, Workout_template, Week
# Register your models here.

admin.site.register(Workout)
admin.site.register(Week)
admin.site.register(Workout_template)