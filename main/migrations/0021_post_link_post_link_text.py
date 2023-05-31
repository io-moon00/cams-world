# Generated by Django 4.1.4 on 2023-04-16 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_rename_category_post_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='link_text',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]