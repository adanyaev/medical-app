# Generated by Django 4.0.3 on 2022-04-14 11:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('med', '0009_doctor_specialization'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='event',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='med.event'),
        ),
    ]