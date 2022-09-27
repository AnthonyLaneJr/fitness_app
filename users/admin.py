from django.contrib import admin
from .models import AgeGroup, FitnessUser, Gender
from workout.models import Workout_template
# Register your models here.


# ------  not functioning ------ #
class FitnessUserAdmin(admin.ModelAdmin):
    prepopulated_fields = {"template_id": '(Workout_template.objects.get(frequency = "exercise_frequency", goal = "goal" ).pk)'}


admin.site.register(AgeGroup)
admin.site.register(FitnessUser)
admin.site.register(Gender)
