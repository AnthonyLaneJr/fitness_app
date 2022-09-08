from multiprocessing import context
from typing import List
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
from .models import Frequency, Gender, AgeGroup, CustomUser, FitnessUser, Goal


class StartPageView(TemplateView):
    template_name = "users/start.html"

class HomePageView(TemplateView):
    template_name = "users/home.html"

class HelpPageView(LoginRequiredMixin ,DetailView):
    template_name = "users/help_page.html"

class NutritionalPageView(LoginRequiredMixin ,DetailView):
    template_name = "users/nutritional.html"

class RegistrationPageView(CreateView):
    template_name = "registration/register.html"

class PasswordResetPageView(UpdateView):
    template_name = "registration/password_reset_form.html"
    success_url = reverse_lazy('start')

class PasswordChangePageView(LoginRequiredMixin ,UpdateView):
    template_name = "registration/password_change_form.html"


'''##############   Below is already completed   #############'''



class AccountDetailView(LoginRequiredMixin, DetailView):
    model = CustomUser
    template_name = "users/view_account.html"


class SettingsPageView(LoginRequiredMixin, TemplateView):
    model = CustomUser
    template_name = "users/settings.html"

class UpdateAccountPageView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    template_name = "users/view_account.html"
    fields = [
        'age_category', 'height', 'gender', 'first_name',
        'last_name', 'exercise_frequency', 'goal',
    ]

