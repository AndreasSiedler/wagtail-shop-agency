# Generated by Django 3.0.10 on 2020-10-20 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theme', '0003_auto_20201020_1038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='themesettings',
            name='about_phone',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='About phone'),
        ),
    ]
