# Generated by Django 2.0.2 on 2018-03-10 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_auto_20180310_2137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chargehoraire',
            name='nbrheures',
            field=models.IntegerField(),
        ),
    ]
