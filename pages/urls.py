from django.urls import path
from .views import StartPageView, HelpPageView, NutritionPageView, RegistrationPageView

urlpatterns = [
    path('', StartPageView.as_view(), name='home'),
    path('about/', HelpPageView.as_view(), name='about'),
    path("about/nutrition", NutritionPageView.as_view(), name='nutrition'),
    path('register', RegistrationPageView.as_view(), name='register')
]
 