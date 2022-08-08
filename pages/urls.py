from django.urls import path
from .views import StartPageView, HelpPageView, NutritionPageView

urlpatterns = [
    path('', StartPageView.as_view(), name='home'),
    path('about/', HelpPageView.as_view(), name='about'),
    path("about/nutrition", NutritionPageView.as_view(), name='nutrition')
]
 