from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
# Create your models here.

class Workout(models.Model):
    def __init__(self):
        super().__init__()
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
    goal_focus = ''


    def goal(self, input):
        if input.lower() == 'weight loss':
            self.goal_focus = input
        if input.lower() == 'weight gain':
            self.goal_focus = input
        else:
            self.goal_focus = 'maintain weight'

    def update_workout(self):
        if self.completed_status == False:
            self.completed_status = True
        else:
            self.completed_status = False

class Workout_template(Workout):
    def __init__(self):
        super().__init__()
    goal = ''
    name = goal
    week_1 = []
    week_2 = []
    week_3 = []
    week_4 = []


    def goal_choice(self, answer):
        if answer == 'weight loss':
            return answer
        elif answer == 'weight gain':
            return answer
        else:
            return 'maintain weight'


    def append_workout(self, workout, week):
        if week == 1:
            self.week_1.append(workout)
        elif week == 2:
            self.week_2.append(workout)
        elif week == 3:
            self.week_3.append(workout)
        elif week == 4:
            self.week_4.append(workout)
        else:
            return 'Please enter a valid week.'
    
