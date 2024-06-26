# Generated by Django 5.0.4 on 2024-05-06 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DatasetEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('notes', models.TextField(blank=True)),
                ('moca', models.CharField(blank=True, max_length=100)),
                ('exercise', models.CharField(blank=True, max_length=100)),
                ('b', models.CharField(blank=True, max_length=100)),
                ('biosense', models.CharField(blank=True, max_length=100)),
                ('breakfast_ace', models.IntegerField(blank=True, null=True)),
                ('lunch_ace', models.IntegerField(blank=True, null=True)),
                ('dinner_ace', models.IntegerField(blank=True, null=True)),
                ('meals', models.CharField(blank=True, max_length=100)),
                ('breakfast', models.CharField(blank=True, max_length=100)),
                ('lunch', models.CharField(blank=True, max_length=100)),
                ('dinner', models.CharField(blank=True, max_length=100)),
                ('supplements', models.CharField(blank=True, max_length=100)),
                ('omega_3', models.CharField(blank=True, max_length=100)),
                ('iron', models.CharField(blank=True, max_length=100)),
                ('b1', models.CharField(blank=True, max_length=100)),
                ('d', models.CharField(blank=True, max_length=100)),
                ('synapsin', models.CharField(blank=True, max_length=100)),
                ('hormones', models.CharField(blank=True, max_length=100)),
                ('thyroid', models.CharField(blank=True, max_length=100)),
                ('estradiol', models.CharField(blank=True, max_length=100)),
                ('progesterone', models.CharField(blank=True, max_length=100)),
                ('mycotoxin_binders', models.CharField(blank=True, max_length=100)),
                ('sac_b', models.CharField(blank=True, max_length=100)),
                ('nac', models.CharField(blank=True, max_length=100)),
                ('charcoal', models.CharField(blank=True, max_length=100)),
                ('bentonite_clay', models.CharField(blank=True, max_length=100)),
                ('optifibre', models.CharField(blank=True, max_length=100)),
                ('interfase_plus', models.CharField(blank=True, max_length=100)),
                ('welchol', models.CharField(blank=True, max_length=100)),
                ('itraconazole', models.CharField(blank=True, max_length=100)),
                ('nystain_oral', models.CharField(blank=True, max_length=100)),
                ('nystatin_nasal', models.CharField(blank=True, max_length=100)),
                ('medication', models.CharField(blank=True, max_length=100)),
                ('code_gg', models.CharField(blank=True, max_length=100)),
                ('code_mm', models.CharField(blank=True, max_length=100)),
                ('code_zz', models.CharField(blank=True, max_length=100)),
                ('code_ss', models.CharField(blank=True, max_length=100)),
                ('fsm_protocol', models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]
