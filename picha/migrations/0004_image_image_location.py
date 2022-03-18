# Generated by Django 3.2.8 on 2021-10-08 18:40

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('picha', '0003_image_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='image_location',
            field=models.ForeignKey(null=True, blank=True, on_delete=django.db.models.deletion.CASCADE, to='picha.location'),
            preserve_default=False,
        ),
    ]
