# Generated by Django 5.1 on 2024-09-02 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='image',
            field=models.ImageField(default='', upload_to='photo/%Y/%m/%d/'),
            preserve_default=False,
        ),
    ]
