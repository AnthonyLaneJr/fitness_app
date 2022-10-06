from  django.contrib.auth.forms import (
    UserChangeForm,
    UserCreationForm,
    AuthenticationForm,
    PasswordChangeForm,
    PasswordResetForm,)
from .models import FitnessUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = FitnessUser
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'goal', 'gender', 'age_category', 'weight', 'height', 'exercise_frequency', 'email',) # meta field --'username', 'password1', 'password2'--

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = FitnessUser
        fields = ('goal', 'gender', 'age_category', 'exercise_frequency', 'weight', 'height', 'template_id', 'email',)
        exclude = ('template_id',)
        UserChangeForm.password = None

class UserLoginForm(AuthenticationForm):
    model = FitnessUser
    fields = ('username', 'password',)
