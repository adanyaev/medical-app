# Generated by Django 4.0.3 on 2022-05-06 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('med', '0003_clinic_address_clinic_specialization'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='specialization',
            field=models.CharField(default='', max_length=35),
        ),
    ]
