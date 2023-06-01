# Generated by Django 4.1.7 on 2023-03-03 00:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Athlet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('forename', models.CharField(max_length=100)),
                ('surename', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CareerStage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=12)),
                ('text', models.TextField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ContactData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('page', models.CharField(choices=[('home', 'Home'), ('about', 'About me'), ('coaching', 'Coaching'), ('athleths', 'Athlets'), ('blog', 'Blog'), ('contact', 'Contact'), ('impressum', 'Impressum'), ('legal', 'Data protection')], default='home', max_length=20)),
                ('hero', models.ImageField(default='../static/img/hero.jpg', upload_to='uploads/')),
                ('hero_alt', models.CharField(default='', max_length=50)),
                ('text', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('postDate', models.DateField(default=datetime.date.today)),
                ('content', models.TextField()),
            ],
        ),
    ]
