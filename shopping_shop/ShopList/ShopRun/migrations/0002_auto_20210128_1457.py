# Generated by Django 3.1.5 on 2021-01-28 05:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ShopRun', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shop',
            old_name='field',
            new_name='message',
        ),
    ]
