from django.urls import path
from .views import WeeklyListView, WorkoutDetailView

urlpatterns = [    
    path('template/daily', WorkoutDetailView.as_view(), name='daily'),
    path('template/weekly', WeeklyListView.as_view(), name='weekly'),
]