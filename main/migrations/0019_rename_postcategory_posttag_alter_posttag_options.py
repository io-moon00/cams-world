# Generated by Django 4.1.4 on 2023-04-16 10:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_alter_postcategory_options_athlet_published_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PostCategory',
            new_name='PostTag',
        ),
        migrations.AlterModelOptions(
            name='posttag',
            options={},
        ),
    ]