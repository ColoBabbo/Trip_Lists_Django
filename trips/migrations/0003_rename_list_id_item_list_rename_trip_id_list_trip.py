# Generated by Django 5.0.6 on 2024-07-02 19:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0002_rename_packing_list_list_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='list_id',
            new_name='list',
        ),
        migrations.RenameField(
            model_name='list',
            old_name='trip_id',
            new_name='trip',
        ),
    ]