# Generated by Django 4.0.2 on 2022-02-11 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content',
            field=models.TextField(default=12),
            preserve_default=False,
        ),
    ]
