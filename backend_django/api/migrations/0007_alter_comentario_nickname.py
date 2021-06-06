# Generated by Django 3.2.4 on 2021-06-06 05:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_comentario_nickname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='nickname',
            field=models.CharField(max_length=8, validators=[django.core.validators.RegexValidator('^[0-9A-Za-z]*$', 'Solo carácteres alfanuméricos son permitidos.')]),
        ),
    ]
