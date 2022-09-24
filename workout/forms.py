from  django.contrib.auth.forms import UserChangeForm
from .models import SingleWorkout


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = SingleWorkout
        fields = ('completed_status',)
        UserChangeForm.password = None 