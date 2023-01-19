# Generated by Django 3.0.14 on 2023-01-16 16:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0041_alter_admins_totalprice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admins',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='order',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=15)),
                ('Email', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=15)),
                ('phonenumber', models.CharField(max_length=10)),
                ('Admins', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Admins')),
            ],
        ),
    ]