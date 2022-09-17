from django.urls import path
from .views import (
    AccountTemplateView, SettingsPageView, UpdateAccountPageView, StartPageView, HomePageView, HelpPageView, NutritionalPageView, RegistrationPageView, PasswordChangePageView, PasswordResetPageView
)
"""
I added the following to the import inorder for it work... StartPageView, HomePageView, HelpPageView, NutritionalPageView, RegistrationPageView, PasswordChangePageView, PasswordResetPageView
"""
urlpatterns = [
    path('', StartPageView.as_view(), name='start'),
    path('home/', HomePageView.as_view(), name='home'),
    path('about/', HelpPageView.as_view(), name='about'),
    path("about/nutrition/", NutritionalPageView.as_view(), name='nutrition'),
    path('register/', RegistrationPageView.as_view(), name='register'),
    path('register/change/', PasswordChangePageView.as_view(), name='change_password'),
    path('register/reset', PasswordResetPageView.as_view(), name='reset_password'),
    path('account/', AccountTemplateView.as_view(), name='account'),
    path('account/update/<int:pk>/', UpdateAccountPageView.as_view(), name='update_account'),
    path('account/settings/', SettingsPageView.as_view(), name='settings'),
]
