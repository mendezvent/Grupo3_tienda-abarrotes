# Generated by Django 4.2.5 on 2023-09-12 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='sexo',
            field=models.CharField(default=2, max_length=50),
            preserve_default=False,
        ),
    ]