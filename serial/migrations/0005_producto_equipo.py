# Generated by Django 2.2.6 on 2019-10-31 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serial', '0004_auto_20191031_1906'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='equipo',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]