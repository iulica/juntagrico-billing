# Generated by Django 3.1.1 on 2020-11-25 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('juntagrico_billing', '0006_auto_20201103_1521'),
    ]

    operations = [
        migrations.AddField(
            model_name='bill',
            name='notification_sent',
            field=models.BooleanField(default=False, verbose_name='Notification sent'),
        ),
    ]