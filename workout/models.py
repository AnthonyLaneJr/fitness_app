from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.  
class Workout_template(models.Model):
    class Purpose(models.IntegerChoices):
        Weight_loss = 0,('Weight Loss')
        Weight_gain = 1,('Weight gain')
        Weight_maintenance = 3,('Weight Maintenance')
    class Frequency(models.IntegerChoices):
        minimal = 0,('1x-2x a week.')
        moderate = 1,('3x-4x a week.')
        intense = 2,('5x-6x a week.')

    name = models.CharField(max_length=128, default='test template')
    purpose = models.IntegerField(default=Purpose.Weight_maintenance ,choices=Purpose.choices)
    frequency = models.IntegerField(default=1 ,choices=Frequency.choices)
    def __str__(self): 
        return self.name

    def goal_choice(self, answer):
        if answer == 'weight loss':
            return answer
        elif answer == 'weight gain':
            return answer
        else:
            return 'maintain weight'


class Week(models.Model):
    name = models.CharField(max_length=128, default='test template')
    goal = models.IntegerField(default=1 ,choices=Workout_template.Purpose.choices)
    template = models.ManyToManyField(Workout_template)
    
    def __str__(self):
        return self.name


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
    completed_status = models.BooleanField(default=False)
    template_week =  models.ManyToManyField(Week)

    def __str__(self):
        return self.name

    def update_workout(self):
        if self.completed_status == False:
            self.completed_status = True
        else:
            self.completed_status = False
