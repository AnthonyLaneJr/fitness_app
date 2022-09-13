from multiprocessing import context
from typing import List
from urllib import request
from django.views.generic import (
    ListView,
    DetailView,
    UpdateView,
    CreateView,
    DeleteView,
    TemplateView
)
from django.urls import reverse_lazy
from django.core.exceptions import BadRequest, PermissionDenied
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Frequency, Gender, AgeGroup, FitnessUser, Goal
from .forms import CustomUserCreationForm, CustomUserChangeForm


class StartPageView(TemplateView):
    template_name = "users/start.html"

class HomePageView(TemplateView):
    template_name = "users/home.html"

class HelpPageView(LoginRequiredMixin ,DetailView):
    template_name = "users/help_page.html"

class NutritionalPageView(LoginRequiredMixin ,DetailView):
    template_name = "users/nutritional.html"



class PasswordResetPageView(UpdateView):
    template_name = "registration/password_reset_form.html"
    success_url = reverse_lazy('start')

class PasswordChangePageView(LoginRequiredMixin ,UpdateView):
    template_name = "registration/password_change_form.html"


'''##############   Below is already completed   

I changed CustomUser to FitnessUser inorder for it to work...#############'''

class RegistrationPageView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("home")
    template_name = "registration/register.html"

class AccountTemplateView(LoginRequiredMixin, TemplateView):
    model = FitnessUser
    template_name = "users/view_account.html"

    '''def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if context["FitnessUser"] == self.request.user:
            return context'''
# if user is authenticated.


class SettingsPageView(LoginRequiredMixin, TemplateView):
    model = FitnessUser
    template_name = "users/settings.html"

class UpdateAccountPageView(LoginRequiredMixin, UpdateView):
    model = FitnessUser
    form_class = CustomUserChangeForm
    template_name = "users/update_account.html"
    fields = [
        'age_category', 'height', 'gender', 'first_name',
        'last_name', 'exercise_frequency', 'goal',
    ]
    success_url = reverse_lazy("home")


