# Generated by Django 4.1.1 on 2023-02-04 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('msg', '0002_remove_request_accepted_request_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
