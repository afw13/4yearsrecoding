# Generated by Django 5.0.4 on 2024-05-06 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataset', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datasetentry',
            name='breakfast_ace',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='datasetentry',
            name='exercise',
            field=models.TextField(blank=True, max_length=100),
        ),
    ]
