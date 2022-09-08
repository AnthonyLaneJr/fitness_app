from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from users.models import Goal
# Create your models here.

class SingleWorkout(models.Model):
    name = models.CharField(max_length=128)
    exercise_1 = models.TextField()
    description_1 = models.TextField()
    exercise_2 = models.TextField()
    description_2 = models.TextField()
    exercise_3 = models.TextField()
    description_3 = models.TextField()
    exercise_4 = models.TextField()
    description_4 = models.TextField()
    exercise_5 = models.TextField()
    description_5 = models.TextField()
    completed_status = False

    def __str__(self):
        return self.name

    def update_workout(self):
        if self.completed_status == False:
            self.completed_status = True
        else:
            self.completed_status = False

class Week(models.Model):
    name = models.CharField(max_length=128, default='test template')
    workouts = []
    
    def __str__(self):
        return self.name

    def append_workout(self, workout):
        if workout in self.workouts:
            print('Workout already in week')
        else:
            self.workouts.append(workout)

        

class Workout_template(models.Model):
    name = models.CharField(max_length=128, default='test template')
    goal = models.ForeignKey(
        Goal,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    weeks = []

    def __str__(self): 
        return self.name

    def goal_choice(self, answer):
        if answer == 'weight loss':
            return answer
        elif answer == 'weight gain':
            return answer
        else:
            return 'maintain weight'


    def append_weekly_template(self, week):
        if week in self.weeks:
            print('Week already in template')
        else:
            self.weeks.append(week)


    
