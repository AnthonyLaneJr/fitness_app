from django.urls import path
from .views import WeeklyDetailView, WorkoutUpdateView, TemplateListView

urlpatterns = [    
    path('daily/<slug:slug>', WorkoutUpdateView.as_view(), name="daily"),
    path("weekly/<slug:slug>", WeeklyDetailView.as_view(), name="weekly"),
    path('template', TemplateListView.as_view(), name='template'),
]