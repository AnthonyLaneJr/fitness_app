from  django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django import forms

from workout.models import Workout_template
from .models import FitnessUser
from users.models import FitnessUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = FitnessUser
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'goal', 'gender', 'age_category', 'weight', 'height', 'exercise_frequency', 'email',)

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = FitnessUser
        fields = ('goal', 'gender', 'age_category', 'exercise_frequency', 'weight', 'height', 'template_id',)
        exclude = ('template_id',)
        UserChangeForm.password = None
