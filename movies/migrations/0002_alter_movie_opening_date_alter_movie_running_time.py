# Generated by Django 4.0 on 2023-07-24 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='opening_date',
            field=models.DateField(default=''),
        ),
        migrations.AlterField(
            model_name='movie',
            name='running_time',
            field=models.IntegerField(default=0),
        ),
    ]