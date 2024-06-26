# Generated by Django 3.2.8 on 2021-11-18 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('acno', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=6)),
                ('address', models.TextField()),
                ('contactno', models.CharField(max_length=15)),
                ('emailaddress', models.EmailField(max_length=50)),
                ('panno', models.CharField(max_length=10)),
                ('adharno', models.CharField(max_length=12)),
                ('balance', models.IntegerField()),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]
