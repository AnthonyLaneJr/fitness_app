from django.db import models
from django.urls import reverse

# Create your models here.  
class Purpose(models.IntegerChoices):
    weight_loss = 0,('Weight Loss.')
    weight_gain = 1,('Weight Gain.')
    weight_maintenance = 2,('Weight Maintenance.')


class Frequency(models.IntegerChoices):
    minimal = 0,('1x-2x a week.')
    moderate = 1,('3x-4x a week.')
    intense = 2,('5x-6x a week.')

class WeekNumber(models.IntegerChoices):
    first = 1,('Week 1')
    second = 2,('Week 2')
    third = 3,('Week 3')
    Fourth = 4,('Week 4')


class SingleWorkout(models.Model):
    name = models.CharField(max_length=128)
    display_name = models.CharField(max_length=128, default='display name')
    exercise_1 = models.TextField(blank=True)
    description_1 = models.TextField(blank=True)
    exercise_2 = models.TextField(blank=True)
    description_2 = models.TextField(blank=True)
    exercise_3 = models.TextField(blank=True)
    description_3 = models.TextField(blank=True)
    exercise_4 = models.TextField(blank=True)
    description_4 = models.TextField(blank=True)
    exercise_5 = models.TextField(blank=True)
    description_5 = models.TextField(blank=True)
    completed_status = models.BooleanField(default=False)
    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return self.name

    def update_workout(self):
        if self.completed_status == False:
            self.completed_status = True
        else:
            self.completed_status = False

    def get_absolute_url(self):
        return reverse("daily", kwargs={"slug" : self.slug})


class Week(models.Model):
    name = models.CharField(max_length=128, default='test template')
    order = models.IntegerField(default=1, choices=WeekNumber.choices)
    goal = models.IntegerField(default=1, choices=Purpose.choices)
    exercise_list = models.ManyToManyField(SingleWorkout)
    completed_status = models.BooleanField(default=False)
    slug = models.SlugField(null=False, unique=True)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("weekly", kwargs={"slug" : self.slug})


class Workout_template(models.Model):
    name = models.CharField(max_length=128, default='test template')
    goal = models.IntegerField(default=2, choices=Purpose.choices)
    frequency = models.IntegerField(default=1, choices=Frequency.choices)
    weeks = models.ManyToManyField(Week)
    completed_status = models.BooleanField(default=False)

    def __str__(self): 
        return self.name

    def goal_choice(self, answer):
        if answer == 'weight loss':
            return answer
        elif answer == 'weight gain':
            return answer
        else:
            return 'maintain weight'
