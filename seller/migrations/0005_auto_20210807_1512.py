# Generated by Django 3.1.1 on 2021-08-07 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0004_auto_20210730_2349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seller',
            name='latitude',
            field=models.DecimalField(decimal_places=6, max_digits=9, null=True),
        ),
        migrations.AlterField(
            model_name='seller',
            name='longitude',
            field=models.DecimalField(decimal_places=6, max_digits=9, null=True),
        ),
    ]