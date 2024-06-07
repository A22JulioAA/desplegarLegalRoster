# Generated by Django 4.2.11 on 2024-05-31 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_cliente_imagen_perfil'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='imagen_perfil',
            field=models.ImageField(default='images/perfil/default.jpg', max_length=200, upload_to='images/perfil/', verbose_name='Imagen de perfil'),
        ),
    ]