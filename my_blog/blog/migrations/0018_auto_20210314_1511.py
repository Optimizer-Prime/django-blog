# Generated by Django 3.1.7 on 2021-03-14 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_auto_20210314_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='summary',
            field=models.CharField(default='', max_length=255),
        ),
    ]