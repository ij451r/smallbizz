# Generated by Django 3.1.1 on 2021-08-08 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0008_seller_storelogo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seller',
            name='StoreLogo',
            field=models.ImageField(default='logo.jpg', upload_to='profile_logo'),
        ),
    ]