# Generated by Django 3.0.3 on 2020-02-24 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reading', '0002_auto_20200224_2101'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='as_draft',
            field=models.BooleanField(default=False),
        ),
    ]
