# Generated by Django 4.1.1 on 2022-09-22 20:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsList', '0015_alter_item_by_customitem'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomItem',
        ),
    ]