# Generated by Django 5.1.3 on 2024-11-29 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0029_alter_myimage_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myimage',
            name='ordering',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
    ]
