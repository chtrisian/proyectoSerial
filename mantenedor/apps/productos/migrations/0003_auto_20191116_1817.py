# Generated by Django 2.2.7 on 2019-11-16 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0002_auto_20191116_1811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen_front',
            field=models.ImageField(blank=True, null=True, upload_to='imagen/productos'),
        ),
    ]