# Generated by Django 4.0.6 on 2022-07-23 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appx', '0002_remove_student_password2'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='project_desc',
            field=models.CharField(blank=True, default='', max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='project_name',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='project_tags',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
    ]
