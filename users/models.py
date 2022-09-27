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

    # trying to automatically assign the temaplate id to this attribute within my user model. This will be based off of the users goal and frequencies which are both imports from the workout application and are uniqely referenced in each template. Meaning each frequency and goal type has a match, Trying to brainstorm a way to automate the foreign key assignmnet based on a matching goal frequency, that is set during the users account creation and/or user account update.
    template_id = models.ForeignKey(
        Workout_template,
        on_delete=models.CASCADE,
        blank=True,
        null=True
        )

    # trying to automatically assign the single workout(s) to this attribute within my user model. The ideal is then during template rendering to compare the completed workouts to the users template to determine whether they have or haven't completed said workout. This is currently being worked on in the WokroutDetailView in the workout applications views.py
    completed_workouts = models.ManyToManyField(SingleWorkout)

    def get_absolute_url(self):
        return reverse('detail', args=[self.id])
