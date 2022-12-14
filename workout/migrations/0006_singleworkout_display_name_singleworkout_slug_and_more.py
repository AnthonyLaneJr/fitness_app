# Generated by Django 4.1.1 on 2022-09-22 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workout', '0005_remove_singleworkout_template_week_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='singleworkout',
            name='display_name',
            field=models.CharField(default='display name', max_length=128),
        ),
        migrations.AddField(
            model_name='singleworkout',
            name='slug',
            field=models.SlugField(null=True),
        ),
        migrations.AddField(
            model_name='week',
            name='order',
            field=models.IntegerField(choices=[(1, 'Week 1'), (2, 'Week 2'), (3, 'Week 3'), (4, 'Week 4')], default=1),
        ),
        migrations.AddField(
            model_name='week',
            name='slug',
            field=models.SlugField(null=True),
        ),
        migrations.AlterField(
            model_name='singleworkout',
            name='description_1',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='singleworkout',
            name='description_2',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='singleworkout',
            name='description_3',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='singleworkout',
            name='description_4',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='singleworkout',
            name='description_5',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='singleworkout',
            name='exercise_1',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='singleworkout',
            name='exercise_2',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='singleworkout',
            name='exercise_3',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='singleworkout',
            name='exercise_4',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='singleworkout',
            name='exercise_5',
            field=models.TextField(blank=True),
        ),
    ]
