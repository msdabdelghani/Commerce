# Generated by Django 3.1.7 on 2021-05-05 22:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_auction_listing_categories'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auction_listing',
            name='categories',
        ),
    ]