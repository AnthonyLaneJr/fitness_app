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
from django.core.exceptions import BadRequest, PermissionDenied
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import FitnessUser
from .forms import CustomUserCreationForm, CustomUserChangeForm, UserLoginForm, MyPasswordChangeForm


class HelpPageView(LoginRequiredMixin ,DetailView):
    template_name = "users/help_page.html"

class NutritionalPageView(LoginRequiredMixin ,DetailView):
    template_name = "users/nutritional.html"



class PasswordResetPageView(UpdateView):
    template_name = "registration/password_reset_form.html"
    success_url = reverse_lazy('start')


'''##############   Below is already completed   

I changed CustomUser to FitnessUser inorder for it to work...#############'''

class StartPageView(FormView):
    form_class = UserLoginForm
    success_url = reverse_lazy("home")
    template_name = "users/start.html"


class PasswordChangePageView(LoginRequiredMixin, UpdateView):
    model = FitnessUser
    form_class = MyPasswordChangeForm
    template_name = "registration/password_change_form.html"
    success_url = reverse_lazy("home") 

    def test_func(self):
        return self.request.user == FitnessUser.objects.get(id = self.kwargs['pk'])


    def get_context_data(self, **kwargs):
        context = super(PasswordChangePageView, self).get_context_data(**kwargs)
        context['user'] = FitnessUser.objects.get(username=self.request.user)
        context['form'] = MyPasswordChangeForm(context['user'])
        return context    


    def form_valid(self, form):
        if form.instance.pk != self.request.user.pk:
            raise PermissionDenied(
                "You are not authorized to update this accounts info."
            )
        return super().form_valid(form)


class HomePageView(LoginRequiredMixin ,TemplateView):
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
