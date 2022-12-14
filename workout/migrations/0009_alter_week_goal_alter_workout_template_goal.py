# Generated by Django 4.1.1 on 2022-09-24 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workout', '0008_alter_singleworkout_slug_alter_week_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='week',
            name='goal',
            field=models.IntegerField(choices=[(0, 'Weight Loss.'), (1, 'Weight Gain.'), (2, 'Weight Maintenance.')], default=1),
        ),
        migrations.AlterField(
            model_name='workout_template',
            name='goal',
            field=models.IntegerField(choices=[(0, 'Weight Loss.'), (1, 'Weight Gain.'), (2, 'Weight Maintenance.')], default=2),
        ),
    ]
