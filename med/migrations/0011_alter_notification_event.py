# Generated by Django 4.0.3 on 2022-04-14 11:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('med', '0010_alter_notification_event'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='event',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='med.event'),
        ),
    ]
