# Generated by Django 2.2.5 on 2019-12-02 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('safe', '0002_userextension'),
    ]

    operations = [
        migrations.AddField(
            model_name='userextension',
            name='is_stay',
            field=models.BooleanField(default=True),
        ),
    ]