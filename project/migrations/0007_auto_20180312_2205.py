# Generated by Django 2.0.2 on 2018-03-12 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0006_utilisateurs_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='annonce',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('titre', models.CharField(default='NULL', max_length=30)),
                ('texte', models.CharField(default='NULL', max_length=1000)),
            ],
        ),
        migrations.RemoveField(
            model_name='chargehoraire',
            name='Matiere',
        ),
        migrations.RemoveField(
            model_name='utilisateurs',
            name='firstname',
        ),
        migrations.AddField(
            model_name='chargehoraire',
            name='cc',
            field=models.CharField(default='NULL', max_length=4),
        ),
        migrations.AddField(
            model_name='chargehoraire',
            name='departement',
            field=models.CharField(default='NULL', max_length=40),
        ),
        migrations.AddField(
            model_name='chargehoraire',
            name='matiere',
            field=models.CharField(default='NULL', max_length=40),
        ),
        migrations.AddField(
            model_name='chargehoraire',
            name='module',
            field=models.CharField(default='NULL', max_length=30),
        ),
        migrations.AddField(
            model_name='utilisateurs',
            name='departement',
            field=models.CharField(default='NULL', max_length=40),
        ),
        migrations.AddField(
            model_name='utilisateurs',
            name='full_name',
            field=models.CharField(default='NULL', max_length=40),
        ),
        migrations.AddField(
            model_name='utilisateurs',
            name='username',
            field=models.CharField(default='NULL', max_length=30),
        ),
    ]
