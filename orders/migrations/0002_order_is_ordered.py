# Generated by Django 4.2.6 on 2023-11-05 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='is_ordered',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
