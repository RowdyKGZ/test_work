# Generated by Django 3.1.5 on 2021-01-20 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webparser', '0003_auto_20210121_0154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='targeturl',
            name='time_to_work',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
