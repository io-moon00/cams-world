# Generated by Django 4.1.4 on 2023-04-13 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_alter_athlet_hero'),
    ]

    operations = [
        migrations.AddField(
            model_name='athlet',
            name='position',
            field=models.CharField(choices=[('top', 'Top'), ('bottom', 'Bottom'), ('center', 'Center'), ('left', 'Left'), ('right', 'Left')], default='duathlon_triathlon', max_length=20),
        ),
        migrations.AddField(
            model_name='page',
            name='position',
            field=models.CharField(choices=[('top', 'Top'), ('bottom', 'Bottom'), ('center', 'Center'), ('left', 'Left'), ('right', 'Left')], default='duathlon_triathlon', max_length=20),
        ),
    ]