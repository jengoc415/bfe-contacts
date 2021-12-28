# Generated by Django 3.0.8 on 2021-12-27 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('detail', '0003_auto_20211227_2001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detail',
            name='address',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='detail',
            name='birthday',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='detail',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]