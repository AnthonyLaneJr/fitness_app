from  django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django import forms

from workout.models import SingleWorkout, Workout_template
from .models import FitnessUser
from users.models import FitnessUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = FitnessUser
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'goal', 'gender', 'age_category', 'exercise_frequency', 'email',)

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = FitnessUser
        fields = ('goal', 'gender', 'age_category', 'exercise_frequency', 'weight', 'height', 'template_id',)
        exclude = ('template_id',)
        UserChangeForm.password = None

class CustomWorkoutChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = FitnessUser
        fields = ('completed_workouts',)
        exclude = ('completed_workouts',)
        UserChangeForm.password = None

''' -----sample forms for correcting completed workout assignment
class TestForm(forms.Form):
    some_field = forms.ModelChoiceField(queryset=SingleWorkout.objects.get(instance), empty_label=None)


    class RenewBookForm(forms.Form):
    renewal_date = forms.DateField(help_text="Enter a date between now and 4 weeks (default 3).")'''