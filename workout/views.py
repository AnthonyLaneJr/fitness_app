from multiprocessing import context
from urllib import request
from django.views.generic import (
    ListView,
    DetailView,
    UpdateView,
    DeleteView
)
from django.urls import reverse_lazy, reverse
from django.shortcuts import redirect
from django.core.exceptions import BadRequest, PermissionDenied
from django.contrib.auth.mixins import LoginRequiredMixin

from users.models import FitnessUser
from .models import SingleWorkout, Workout_template, Week
# Create your views here.

class WeeklyDetailView(LoginRequiredMixin, DetailView):
    model = Week
    template_name = "workout/weekly_view.html"

    def get_context_data(self, **kwargs):
        context = super(WeeklyDetailView, self).get_context_data(**kwargs)
        context['week'] = Week.objects.get(slug = self.kwargs['slug'])
        return context

class WorkoutDetailView(LoginRequiredMixin, DetailView):
    model = SingleWorkout
    template_name = 'workout/daily_view.html'
    success_url = reverse_lazy("template")

    def get_context_data(self, **kwargs):
        context = super(WorkoutDetailView, self).get_context_data(**kwargs)
        user = FitnessUser.objects.get(pk = self.request.user.pk)
        context['exercise'] = SingleWorkout.objects.get(slug = self.kwargs['slug'])
        context['workouts'] = {}
        for workout in user.completed_workouts.all():
            context['workouts'][workout.name] = workout
        

        return context


def update_workout_data(request, slug):   
    workout = SingleWorkout.objects.get(slug=slug)
    endUser = FitnessUser.objects.get(pk = request.user.pk)
    endUser.completed_workouts.add(workout)
    endUser.save()
    return redirect(reverse('daily', kwargs={'slug':workout.slug}))


class TemplateListView(LoginRequiredMixin, ListView):
    model = Workout_template
    template_name = "workout/template_view.html"

    def get_context_data(self, **kwargs):
        context = super(TemplateListView, self).get_context_data(**kwargs)
        context['template'] = Workout_template.objects.get(name = self.request.user.template_id)
        return context

