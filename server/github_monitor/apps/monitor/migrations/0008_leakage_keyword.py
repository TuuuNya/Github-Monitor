# Generated by Django 2.0 on 2018-10-17 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0007_remove_leakage_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='leakage',
            name='keyword',
            field=models.CharField(default='', max_length=256, null=True),
        ),
    ]
