# Generated by Django 4.1.1 on 2023-02-04 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Connection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user1', models.CharField(max_length=20)),
                ('user2', models.CharField(max_length=20)),
                ('connected', models.BooleanField(default='False')),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.CharField(max_length=20)),
                ('reciever', models.CharField(max_length=20)),
                ('accepted', models.BooleanField(default='False')),
            ],
        ),
    ]