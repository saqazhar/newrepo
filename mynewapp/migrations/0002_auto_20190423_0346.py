# Generated by Django 2.0 on 2019-04-23 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mynewapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myform',
            name='phone',
            field=models.IntegerField(),
        ),
    ]