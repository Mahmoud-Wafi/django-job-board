# Generated by Django 5.1 on 2024-09-01 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('job_type', models.CharField(choices=[('Full Time', 'Full Time'), ('Part Time', 'Part Time')], max_length=15)),
                ('description', models.TextField()),
                ('publishAt', models.DateTimeField(auto_now=True)),
                ('vacancy', models.IntegerField(default=1, max_length=4)),
                ('salary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('experience', models.IntegerField(default=1)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10)),
            ],
        ),
    ]
