# Generated by Django 4.1.1 on 2022-09-24 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_remove_fitnessuser_template_fitnessuser_template_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fitnessuser',
            name='goal',
            field=models.IntegerField(choices=[(0, 'Weight Loss.'), (1, 'Weight Gain.'), (2, 'Weight Maintenance.')], default=1),
        ),
    ]
