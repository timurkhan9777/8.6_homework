# Generated by Django 5.0.6 on 2024-07-03 10:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hudud',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('created', models.DateField()),
                ('hudud', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='building.hudud')),
            ],
        ),
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('field', models.IntegerField()),
                ('floor', models.IntegerField()),
                ('parking', models.BooleanField()),
                ('playground', models.BooleanField()),
                ('lift', models.BooleanField()),
                ('hudud', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='building.hudud')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='building.organization')),
            ],
        ),
    ]
