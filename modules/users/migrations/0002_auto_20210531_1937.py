# Generated by Django 3.2.3 on 2021-06-01 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='id',
            field=models.IntegerField(auto_created=True, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='country',
            name='id',
            field=models.IntegerField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]