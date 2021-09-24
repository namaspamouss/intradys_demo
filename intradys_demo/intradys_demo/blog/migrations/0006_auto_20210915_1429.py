# Generated by Django 3.2.7 on 2021-09-15 12:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20210915_1351'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='color', max_length=32)),
                ('value', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='blog.color')),
            ],
        ),
        migrations.DeleteModel(
            name='ColorSettings',
        ),
    ]
