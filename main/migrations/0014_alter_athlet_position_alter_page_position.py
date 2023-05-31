# Generated by Django 4.1.4 on 2023-04-13 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_athlet_position_page_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='athlet',
            name='position',
            field=models.CharField(choices=[('top', 'Top'), ('bottom', 'Bottom'), ('center', 'Center'), ('left', 'Left'), ('right', 'Left')], default='center', max_length=20),
        ),
        migrations.AlterField(
            model_name='page',
            name='position',
            field=models.CharField(choices=[('top', 'Top'), ('bottom', 'Bottom'), ('center', 'Center'), ('left', 'Left'), ('right', 'Left')], default='center', max_length=20),
        ),
    ]
