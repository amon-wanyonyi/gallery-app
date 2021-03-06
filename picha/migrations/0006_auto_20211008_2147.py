# Generated by Django 3.2.8 on 2021-10-08 18:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('picha', '0005_image_image_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image_category',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='picha.category'),
        ),
        migrations.AlterField(
            model_name='image',
            name='image_location',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='picha.location'),
        ),
    ]
