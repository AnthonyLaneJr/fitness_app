from multiprocessing import context
from urllib import request
from django.views.generic import (
    DetailView,
    UpdateView,
    CreateView,
    TemplateView,
    FormView
)
from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from django.core.exceptions import BadRequest, PermissionDenied
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import FitnessUser
from .forms import CustomUserCreationForm, CustomUserChangeForm, UserLoginForm
from django.urls import reverse_lazy, reverse


class HelpPageView(LoginRequiredMixin, DetailView):
    template_name = "users/help_page.html"

class NutritionalPageView(LoginRequiredMixin, TemplateView):
    template_name = "users/nutritional.html"



'''##############   Below is already completed   

I changed CustomUser to FitnessUser inorder for it to work...#############'''

class StartPageView(FormView):
    form_class = UserLoginForm
    success_url = reverse_lazy("home")
    template_name = "users/start.html"


class HomePageView(LoginRequiredMixin, TemplateView):
    template_name = "users/home.html"


class RegistrationPageView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("home")
    template_name = "registration/register.html"


class AccountTemplateView(LoginRequiredMixin, TemplateView):
    model = FitnessUser
    template_name = "users/view_account.html"

    def get_context_data(self, **kwargs):
        user = FitnessUser.objects.get(username=self.request.user)
        return super().get_context_data(**kwargs)


class SettingsPageView(LoginRequiredMixin, TemplateView):
    model = FitnessUser
    template_name = "users/settings.html"

    def get_context_data(self, **kwargs):
        user = FitnessUser.objects.get(username=self.request.user)
        return super().get_context_data(**kwargs)


def remove_workout_data(request):   
    endUser = FitnessUser.objects.get(pk = request.user.pk)
    endUser.completed_workouts.clear()
    endUser.save()
    return redirect(reverse('template'))


class UpdateAccountPageView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = FitnessUser
    form_class = CustomUserChangeForm
    template_name = "users/update_account.html"
    success_url = reverse_lazy("home")

    def test_func(self):
        return self.request.user == FitnessUser.objects.get(id = self.kwargs['pk'])


    def get_context_data(self, **kwargs):
        user = FitnessUser.objects.get(username=self.request.user)
        return super().get_context_data(**kwargs)


    def form_valid(self, form):
        if form.instance.pk != self.request.user.pk:
            raise PermissionDenied(
                "You are not authorized to update this accounts info."
            )
        return super().form_valid(form)


def custom_403_error_page(request, exception):
    return render(request, 'users/403.html', {})


def custom_405_error_page(request, exception):
    return render(request, 'users/405.html', {})
