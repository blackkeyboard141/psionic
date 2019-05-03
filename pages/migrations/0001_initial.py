# Generated by Django 2.2.1 on 2019-05-03 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Userdata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('pnumber', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('dob', models.DateField(max_length=8)),
            ],
        ),
    ]