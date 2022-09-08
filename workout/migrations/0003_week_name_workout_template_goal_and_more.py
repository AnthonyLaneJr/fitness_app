# Generated by Django 4.1.1 on 2022-09-08 02:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_remove_fitnessuser_description'),
        ('workout', '0002_rename_workout_singleworkout'),
    ]

    operations = [
        migrations.AddField(
            model_name='week',
            name='name',
            field=models.CharField(default='test template', max_length=128),
        ),
        migrations.AddField(
            model_name='workout_template',
            name='goal',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.goal'),
        ),
        migrations.AddField(
            model_name='workout_template',
            name='name',
            field=models.CharField(default='test template', max_length=128),
        ),
    ]