# Generated by Django 4.1.4 on 2023-02-22 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BheemaGF',
            fields=[
                ('instaId', models.IntegerField(primary_key=True, serialize=False)),
                ('gfname', models.CharField(max_length=100)),
                ('mobile', models.IntegerField()),
            ],
        ),
    ]
