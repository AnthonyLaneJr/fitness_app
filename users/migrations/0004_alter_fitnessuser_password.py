# Generated by Django 4.1.1 on 2022-09-15 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_remove_fitnessuser_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fitnessuser',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
    ]