# Generated by Django 3.1.7 on 2021-03-14 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_auto_20210314_1509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='summary',
            field=models.CharField(default='<django.db.models.fields.CharField>', max_length=255),
        ),
    ]
