# Generated by Django 4.1.2 on 2024-10-20 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_alter_order_address_alter_order_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='payment_status',
            field=models.CharField(default='Unpaid', max_length=10),
        ),
    ]
