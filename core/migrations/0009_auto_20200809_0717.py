# Generated by Django 3.0.8 on 2020-08-09 07:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problems',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.UserProfile'),
        ),
    ]
