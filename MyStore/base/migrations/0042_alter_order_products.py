# Generated by Django 4.1.4 on 2023-01-10 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0041_alter_admins_totalprice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(related_name='product', to='base.product'),
        ),
    ]
