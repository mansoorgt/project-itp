# Generated by Django 4.0.4 on 2023-04-11 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0007_speakerregistrations_deleted'),
    ]

    operations = [
        migrations.AddField(
            model_name='speakerregistrations',
            name='remark',
            field=models.TextField(default='', null=True),
        ),
    ]
