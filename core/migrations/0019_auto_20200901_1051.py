# Generated by Django 3.0 on 2020-09-01 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_merge_20200823_0858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problems',
            name='device_brand',
            field=models.CharField(blank=True, choices=[('T', 'Teckno'), ('S', 'Samsung'), ('U', 'Huawei'), ('I', 'Iphone')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='problems',
            name='device_type',
            field=models.CharField(blank=True, choices=[('A', 'Android')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='expert_to',
            field=models.CharField(blank=True, choices=[('T', 'Teckno'), ('S', 'Samsung'), ('U', 'Huawei'), ('I', 'Iphone')], max_length=200, null=True),
        ),
    ]
