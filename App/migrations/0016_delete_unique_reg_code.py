# Generated by Django 4.0.4 on 2023-04-27 07:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0015_alter_unique_reg_code_urcode'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Unique_reg_code',
        ),
    ]