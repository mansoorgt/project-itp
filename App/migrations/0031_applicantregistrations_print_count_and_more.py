# Generated by Django 4.0.4 on 2023-05-11 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0030_invitedregistrations_urc_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicantregistrations',
            name='print_count',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='invitedregistrations',
            name='print_count',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='speakerregistrations',
            name='print_count',
            field=models.IntegerField(null=True),
        ),
    ]
