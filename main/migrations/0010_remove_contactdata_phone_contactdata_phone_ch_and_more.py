# Generated by Django 4.1.4 on 2023-04-11 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_page_title_de_alter_post_content_de_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactdata',
            name='phone',
        ),
        migrations.AddField(
            model_name='contactdata',
            name='phone_ch',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='contactdata',
            name='phone_de',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
