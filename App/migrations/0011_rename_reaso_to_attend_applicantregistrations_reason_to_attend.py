# Generated by Django 3.2.16 on 2023-04-25 06:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0010_applicantregistrations'),
    ]

    operations = [
        migrations.RenameField(
            model_name='applicantregistrations',
            old_name='reaso_to_attend',
            new_name='reason_to_attend',
        ),
    ]
