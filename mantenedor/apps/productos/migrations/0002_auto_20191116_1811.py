# Generated by Django 2.2.7 on 2019-11-16 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen_back',
            field=models.ImageField(blank=True, null=True, upload_to='imagen/productos'),
        ),
    ]
