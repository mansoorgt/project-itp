# Generated by Django 4.0.4 on 2023-04-27 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0013_unique_reg_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unique_reg_code',
            name='urcode',
            field=models.CharField(default='B4DE4', editable=False, max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterModelTable(
            name='unique_reg_code',
            table='app_unique_reg_code',
        ),
    ]