# Generated by Django 4.1.1 on 2022-09-21 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsList', '0009_alter_item_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='id',
            field=models.IntegerField(editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
