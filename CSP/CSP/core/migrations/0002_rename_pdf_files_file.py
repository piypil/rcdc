# Generated by Django 4.2.2 on 2023-06-14 07:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='files',
            old_name='pdf',
            new_name='file',
        ),
    ]
