# Generated by Django 4.1.4 on 2023-01-08 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0040_alter_admins_totalprice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admins',
            name='totalprice',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
