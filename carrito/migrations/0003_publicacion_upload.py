# Generated by Django 4.1.5 on 2023-06-19 22:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('carrito', '0002_publicacion_delete_carrito'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicacion',
            name='upload',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='static/img/'),
            preserve_default=False,
        ),
    ]
