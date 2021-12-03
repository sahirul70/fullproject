# Generated by Django 3.2.9 on 2021-11-17 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indexpage', '0007_appointment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=50)),
                ('massage', models.TextField()),
            ],
        ),
    ]
