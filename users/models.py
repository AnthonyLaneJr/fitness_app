from email.policy import default
from django.urls import reverse
from django.db import models
from django.contrib.auth.models import AbstractUser
from workout.models import Frequency, Purpose, SingleWorkout, Workout_template

class Gender(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class AgeGroup(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class FitnessUser(AbstractUser):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=60)
    age_category = models.ForeignKey(
        AgeGroup,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    goal = models.IntegerField(default=1 ,choices=Purpose.choices)
    weight = models.CharField(max_length=30)
    height = models.CharField(max_length=30)
    gender = models.ForeignKey(
        Gender,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    exercise_frequency = models.IntegerField(default=1 ,choices=Frequency.choices)
    template_id = models.ForeignKey(
        Workout_template,
        on_delete=models.CASCADE,
        blank=True,
        null=True
        )
    completed_workouts = models.ManyToManyField(SingleWorkout)

    def get_absolute_url(self):
        return reverse('detail', args=[self.id])
