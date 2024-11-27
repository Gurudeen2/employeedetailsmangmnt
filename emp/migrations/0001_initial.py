# Generated by Django 4.1 on 2024-11-20 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('age', models.CharField(blank=True, max_length=10)),
                ('gender', models.CharField(blank=True, max_length=10)),
                ('phone', models.CharField(max_length=10)),
                ('department', models.CharField(max_length=200)),
                ('religion', models.CharField(max_length=20)),
                ('qualification', models.TextField(blank=True)),
                ('client', models.CharField(max_length=100)),
                ('experience', models.TextField(blank=True)),
                ('photo', models.ImageField(blank=True, upload_to='photo/%Y/%m/%d/')),
                ('date_startwork', models.DateField()),
            ],
        ),
    ]
