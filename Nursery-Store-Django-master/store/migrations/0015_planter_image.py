# Generated by Django 4.1.2 on 2024-10-21 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0014_remove_planter_image_alter_category_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='planter',
            name='image',
            field=models.ImageField(blank=True, default='path/to/default/image.jpg', null=True, upload_to='products/'),
        ),
    ]
