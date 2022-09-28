from multiprocessing import context
from urllib import request
from django.views.generic import (
    ListView,
    DetailView,
    UpdateView,
    DeleteView
)
from django.urls import reverse_lazy
from django.core.exceptions import BadRequest, PermissionDenied
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import SingleWorkout, Workout_template, Week
from users.forms import CustomWorkoutChangeForm
# Create your views here.

class WeeklyDetailView(LoginRequiredMixin, DetailView):
    model = Week
    template_name = "workout/weekly_view.html"

    def get_context_data(self, **kwargs):
        context = super(WeeklyDetailView, self).get_context_data(**kwargs)
        context['week'] = Week.objects.get(slug = self.kwargs['slug'])
        return context

class WorkoutUpdateView(LoginRequiredMixin, UpdateView):
    model = SingleWorkout
    template_name = 'workout/daily_view.html'
    form_class = CustomWorkoutChangeForm
    success_url = reverse_lazy("template")

    def get_context_data(self, **kwargs):
        context = super(WorkoutUpdateView, self).get_context_data(**kwargs)
        context['exercise'] = SingleWorkout.objects.get(slug = self.kwargs['slug'])
        return context


class TemplateListView(LoginRequiredMixin, ListView):
    model = Workout_template
    template_name = "workout/template_view.html"

    def get_context_data(self, **kwargs):
        context = super(TemplateListView, self).get_context_data(**kwargs)
        context['template'] = Workout_template.objects.get(name = self.request.user.template_id)
        return context

