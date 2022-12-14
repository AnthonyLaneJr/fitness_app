# Generated by Django 4.1.1 on 2022-09-24 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workout', '0009_alter_week_goal_alter_workout_template_goal'),
        ('users', '0008_alter_fitnessuser_goal'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserList',
        ),
        migrations.AddField(
            model_name='fitnessuser',
            name='completed_workouts',
            field=models.ManyToManyField(to='workout.singleworkout'),
        ),
    ]
