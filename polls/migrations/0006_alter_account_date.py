# Generated by Django 5.0.3 on 2024-03-13 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_alter_account_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
