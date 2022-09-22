from django.contrib import admin
from .models import SingleWorkout, Workout_template, Week
# Register your models here.
class SingleWorkoutAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

class WeekAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(SingleWorkout, SingleWorkoutAdmin)
admin.site.register(Week, WeekAdmin)
admin.site.register(Workout_template)