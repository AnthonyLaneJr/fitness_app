from multiprocessing import context
from typing import List
from django.views.generic import (
    ListView,
    DetailView,
    UpdateView,
    CreateView,
    DeleteView
)
from django.urls import reverse_lazy
from django.core.exceptions import BadRequest, PermissionDenied
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Workout, Workout_template
# Create your views here.

class WeeklyListView(LoginRequiredMixin, ListView):
    model = Workout_template
    template_name = "workout/weekly_view.html"

    def get_weekly_exercise_list(self, context, name, week):
        context['workout_list'] = Workout_template.objects.filter(
            name=name
        ).filter(week=Workout_template.weeks[week])
        return context

class WorkoutDetailView(LoginRequiredMixin, DetailView):
    model = Workout_template
    template_name = 'workout/daily_view.html'

    def get_daily_exercise(self, context, name, week, index):
        context['workout'] = Workout_template.objects.filter(
            name=name
        ).filter(week=Workout_template.weeks[week]).filter(
            index = week[index])
        return context


