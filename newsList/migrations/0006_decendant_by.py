# Generated by Django 4.1.1 on 2022-09-19 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsList', '0005_rename_decendants_item_descendants'),
    ]

    operations = [
        migrations.AddField(
            model_name='decendant',
            name='by',
            field=models.CharField(default=2, max_length=50),
            preserve_default=False,
        ),
    ]
