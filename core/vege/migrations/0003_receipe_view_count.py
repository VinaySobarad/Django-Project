# Generated by Django 5.1.3 on 2024-11-15 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0002_receipe_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='receipe',
            name='view_count',
            field=models.IntegerField(default=1),
        ),
    ]
