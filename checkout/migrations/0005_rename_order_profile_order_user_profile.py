# Generated by Django 5.1.3 on 2024-12-03 11:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0004_order_order_profile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='order_profile',
            new_name='user_profile',
        ),
    ]
