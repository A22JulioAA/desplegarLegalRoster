# Generated by Django 4.2.11 on 2024-05-30 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_especialidad_parent_alter_profesional_especialidad'),
    ]

    operations = [
        migrations.AddField(
            model_name='profesional',
            name='imagenPerfil',
            field=models.ImageField(default='images/default.jpg', upload_to='images/'),
        ),
    ]
