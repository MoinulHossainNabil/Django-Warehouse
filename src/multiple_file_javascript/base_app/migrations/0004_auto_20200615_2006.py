# Generated by Django 3.0.7 on 2020-06-15 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0003_auto_20200615_2004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
