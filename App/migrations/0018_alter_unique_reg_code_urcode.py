# Generated by Django 4.0.4 on 2023-04-27 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0017_unique_reg_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unique_reg_code',
            name='urcode',
            field=models.UUIDField(default='265279', editable=False, primary_key=True, serialize=False),
        ),
    ]
