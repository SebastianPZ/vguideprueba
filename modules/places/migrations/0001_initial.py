# Generated by Django 3.2.3 on 2021-06-08 00:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('department', models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='places.department')),
            ],
        ),
        migrations.CreateModel(
            name='TypePlace',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('icon', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='TouristicPlace',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('cost_info', models.CharField(max_length=255)),
                ('price', models.FloatField()),
                ('schedule_info', models.CharField(max_length=255)),
                ('historic_info', models.CharField(max_length=255)),
                ('long_info', models.CharField(max_length=255)),
                ('short_info', models.CharField(max_length=255)),
                ('activities_info', models.CharField(max_length=255)),
                ('latitude', models.CharField(max_length=16)),
                ('longitude', models.CharField(max_length=16)),
                ('range', models.IntegerField()),
                ('status', models.IntegerField(default=1)),
                ('province', models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='places.province')),
                ('type_place', models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='places.typeplace')),
            ],
        ),
        migrations.CreateModel(
            name='PictureTouristicPlace',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('url', models.CharField(max_length=255)),
                ('number', models.IntegerField()),
                ('touristic_place', models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='places.touristicplace')),
            ],
        ),
    ]