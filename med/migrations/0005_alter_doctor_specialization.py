# Generated by Django 4.0.3 on 2022-05-06 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('med', '0004_alter_doctor_specialization'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='specialization',
            field=models.CharField(default='', max_length=50),
        ),
    ]
