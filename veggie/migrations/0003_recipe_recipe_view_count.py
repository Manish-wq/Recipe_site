# Generated by Django 5.0.1 on 2024-01-13 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veggie', '0002_recipe_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='recipe_view_count',
            field=models.IntegerField(default=1),
        ),
    ]