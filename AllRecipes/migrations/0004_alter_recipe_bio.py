# Generated by Django 5.0.4 on 2024-06-06 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AllRecipes', '0003_rename_user_recipe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='bio',
            field=models.CharField(max_length=100),
        ),
    ]
