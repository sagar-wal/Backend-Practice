# Generated by Django 2.2.7 on 2019-11-10 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='name',
            field=models.CharField(default='Note', max_length=500),
        ),
        migrations.AlterField(
            model_name='data',
            name='moment',
            field=models.DateTimeField(),
        ),
    ]