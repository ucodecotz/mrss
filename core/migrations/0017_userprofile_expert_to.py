# Generated by Django 3.0 on 2020-08-22 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_comments_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='expert_to',
            field=models.CharField(blank=True, choices=[('T', 'Teckno'), ('S', 'Samsung'), ('U', 'Huawei'), ('O', 'Oppo')], max_length=200, null=True),
        ),
    ]