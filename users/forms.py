from  django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import FitnessUser
from users.models import FitnessUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = FitnessUser
        fields = UserCreationForm.Meta.fields + ('goal', 'gender', 'age_category', 'exercise_frequency')

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = FitnessUser
        fields = UserChangeForm.Meta.fields