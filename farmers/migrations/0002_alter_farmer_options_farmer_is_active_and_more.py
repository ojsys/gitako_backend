# Generated by Django 5.1 on 2024-08-23 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmers', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='farmer',
            options={'verbose_name': 'Farmer', 'verbose_name_plural': 'Farmers'},
        ),
        migrations.AddField(
            model_name='farmer',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='farmer',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='farmer',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='farmer',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
