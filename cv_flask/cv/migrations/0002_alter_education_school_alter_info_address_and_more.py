# Generated by Django 4.1 on 2022-09-03 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='school',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='info',
            name='address',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='title',
            field=models.CharField(max_length=30),
        ),
    ]