from django.urls import path
from .views import WeeklyListView, WorkoutDetailView

urlpatterns = [    
    path('daily', WorkoutDetailView.as_view(), name='daily'),
    path('weekly', WeeklyListView.as_view(), name='weekly'),
]