# Generated by Django 5.0.6 on 2024-07-15 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='people',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
