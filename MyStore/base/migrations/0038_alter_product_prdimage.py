# Generated by Django 4.1.4 on 2023-01-06 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0037_alter_product_prdimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='PRDimage',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]