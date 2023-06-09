# Generated by Django 4.1.4 on 2023-04-11 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_rename_images_athlet_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='athlet',
            old_name='image',
            new_name='hero',
        ),
        migrations.AddField(
            model_name='aboutsection',
            name='text_de',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='aboutsection',
            name='title_de',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='careerstage',
            name='text_de',
            field=models.TextField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='page',
            name='text_de',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='page',
            name='titel_de',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='post',
            name='content_de',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='post',
            name='title_de',
            field=models.CharField(default='', max_length=100),
        ),
    ]
