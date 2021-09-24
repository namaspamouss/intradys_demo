# Generated by Django 3.2.7 on 2021-09-15 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='color',
            name='rgba',
        ),
        migrations.AddField(
            model_name='color',
            name='blue',
            field=models.FloatField(default=1.0),
        ),
        migrations.AddField(
            model_name='color',
            name='green',
            field=models.FloatField(default=1.0),
        ),
        migrations.AddField(
            model_name='color',
            name='red',
            field=models.FloatField(default=1.0),
        ),
    ]