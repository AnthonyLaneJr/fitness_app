from multiprocessing import context
from re import template
from ssl import Purpose
from typing import List
from django.views.generic import (
    ListView,
    DetailView,
    UpdateView,
    DeleteView
)
from django.urls import reverse_lazy
from django.core.exceptions import BadRequest, PermissionDenied
from django.contrib.auth.mixins import LoginRequiredMixin

from users.models import FitnessUser
from .models import SingleWorkout, Workout_template, Week
# Create your views here.

class WeeklyListView(LoginRequiredMixin, ListView):
    model = Workout_template
    template_name = "workout/weekly_view.html"

    def get_context_data(self, **kwargs):
        context = super(WeeklyListView, self).get_context_data(**kwargs)
        context['template'] = Workout_template.objects.filter(purpose=1, frequency=0)
        context['template_weeks'] = []
        return context

class WorkoutDetailView(LoginRequiredMixin, DetailView):
    model = SingleWorkout
    template_name = 'workout/daily_view.html'

    def get_daily_exercise(self, context, name, week, index):
        context['workout'] = Workout_template.objects.filter(
            name=name
        ).filter(week=Workout_template.weeks[week]).filter(
            index = week[index])
        return context


