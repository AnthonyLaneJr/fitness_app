from django.urls import path
from .views import WeeklyDetailView, WorkoutDetailView, TemplateListView, update_workout_data, remove_workout_data

urlpatterns = [    
    path('daily/<slug:slug>', WorkoutDetailView.as_view(), name="daily"),
    path("weekly/<slug:slug>", WeeklyDetailView.as_view(), name="weekly"),
    path('template', TemplateListView.as_view(), name='template'),
    path('update/<slug:slug>', update_workout_data, name='update'),
    path('remove/<slug:slug>', remove_workout_data, name='remove'),
]