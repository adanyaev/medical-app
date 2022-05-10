# Generated by Django 4.0.3 on 2022-05-10 22:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('med', '0007_rename_clinic_doctor_clinics'),
    ]

    operations = [
        migrations.AlterField(
            model_name='treatment',
            name='clinic',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='med.clinic'),
        ),
        migrations.AlterField(
            model_name='treatment',
            name='doctor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='med.doctor'),
        ),
        migrations.AlterField(
            model_name='treatment',
            name='patient',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='med.patient'),
        ),
    ]