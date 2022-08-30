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
from .models import Frequency, Gender, AgeGroup, CustomUser

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
        'last_name', 'exercise_frequency', 'description',
    ]

