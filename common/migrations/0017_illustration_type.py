# Generated by Django 4.2.4 on 2023-12-04 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0016_alter_illustration_updatetime'),
    ]

    operations = [
        migrations.AddField(
            model_name='illustration',
            name='type',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
