# Generated by Django 3.1.1 on 2021-08-08 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0007_auto_20210807_1849'),
    ]

    operations = [
        migrations.AddField(
            model_name='seller',
            name='StoreLogo',
            field=models.ImageField(default='logo.jpg', upload_to=''),
        ),
    ]
