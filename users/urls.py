from django.urls import path
from .views import (
    AccountTemplateView, SettingsPageView, UpdateAccountPageView, StartPageView, HomePageView, HelpPageView, NutritionalPageView, RegistrationPageView, remove_workout_data
)

urlpatterns = [
    path('', StartPageView.as_view(), name='start'),
    path('home/', HomePageView.as_view(), name='home'),
    path('about/', HelpPageView.as_view(), name='about'),
    path("about/nutrition/", NutritionalPageView.as_view(), name='nutrition'),
    path('register/', RegistrationPageView.as_view(), name='register'),
    path('account/', AccountTemplateView.as_view(), name='account'),
    path('account/update/<int:pk>/', UpdateAccountPageView.as_view(), name='update_account'),
    path('account/settings/', SettingsPageView.as_view(), name='settings'),
    path('update/', remove_workout_data, name='update_workouts'),
]
