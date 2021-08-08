# Generated by Django 3.1.1 on 2021-08-07 13:19

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0006_auto_20210807_1513'),
    ]

    operations = [
        migrations.AddField(
            model_name='seller',
            name='Account_created_on',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.CreateModel(
            name='SellerInavailability',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_unavailable', models.DateTimeField()),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seller.seller')),
            ],
        ),
    ]
