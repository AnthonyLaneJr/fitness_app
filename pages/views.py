from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy


class StartPageView(TemplateView):
    template_name = "pages/start.html"

class HomePageView(TemplateView):
    template_name = "pages/home.html"

class HelpPageView(TemplateView):
    template_name = "pages/help_page.html"

class NutritionalPageView(TemplateView):
    template_name = "pages/nutritional.html"

class RegistrationPageView(TemplateView):
    template_name = "registration/register.html"

class PasswordResetPageView(TemplateView):
    template_name = "registration/password_reset_form.html"
    success_url = reverse_lazy('start')

class PasswordChangePageView(TemplateView):
    template_name = "registration/password_change_form.html"

class AccountPageView(TemplateView):
    template_name = "users/view_account.html"

class SettingsPageView(TemplateView):
    template_name = "users/settings.html"

class UpdateAccountPageView(TemplateView):
    template_name = "users/view_account.html"

class DailyPageView(TemplateView):
    template_name = "workouts/daily_view.html"

class WeeklyPageView(TemplateView):
    template_name = "workouts/weekly_view.html"
