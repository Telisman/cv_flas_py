# Generated by Django 4.1 on 2022-09-05 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0006_alter_workexperience_end_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='section',
            field=models.CharField(default=1, max_length=80),
            preserve_default=False,
        ),
    ]
