# Generated by Django 3.2.4 on 2021-06-07 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_auto_20210606_2038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='comentario',
            field=models.CharField(max_length=120),
        ),
    ]
