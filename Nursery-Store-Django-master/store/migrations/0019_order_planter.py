# Generated by Django 4.1.2 on 2024-10-21 08:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0018_planter'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='planter',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='store.planter'),
        ),
    ]
