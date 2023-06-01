# Generated by Django 4.1.7 on 2023-03-03 19:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(default='../../media/uploads/placeholder.jpg', upload_to='uploads/')),
                ('alt', models.CharField(max_length=100)),
            ],
        ),
        migrations.RenameField(
            model_name='athlet',
            old_name='forename',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='athlet',
            old_name='surename',
            new_name='last_name',
        ),
        migrations.RemoveField(
            model_name='page',
            name='hero_alt',
        ),
        migrations.AlterField(
            model_name='page',
            name='page',
            field=models.CharField(choices=[('home', 'Home'), ('about', 'About me'), ('coaching', 'Coaching'), ('athlets', 'Athlets'), ('blog', 'Blog'), ('contact', 'Contact'), ('impressum', 'Impressum'), ('legal', 'Data protection')], default='home', max_length=20),
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.image'),
        ),
        migrations.AlterField(
            model_name='page',
            name='hero',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.image'),
        ),
    ]
