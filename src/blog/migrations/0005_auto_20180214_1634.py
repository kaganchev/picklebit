# Generated by Django 2.0.1 on 2018-02-14 16:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20180214_1631'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='uuid',
            new_name='post_id',
        ),
    ]
