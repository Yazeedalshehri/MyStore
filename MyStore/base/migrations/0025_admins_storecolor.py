# Generated by Django 4.1.4 on 2023-01-05 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0024_remove_admins_category111'),
    ]

    operations = [
        migrations.AddField(
            model_name='admins',
            name='storecolor',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]
