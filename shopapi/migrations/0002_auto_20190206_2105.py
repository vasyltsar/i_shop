# Generated by Django 2.1.5 on 2019-02-06 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='state',
            field=models.CharField(choices=[('NEW', 'new'), ('REFURBISHED', 'refurbished'), ('REVALUATED', 'revaluated')], max_length=255),
        ),
    ]