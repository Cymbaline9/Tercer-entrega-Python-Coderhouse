# Generated by Django 4.2.3 on 2023-08-13 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0004_rename_telefono_alumno_dni_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profesor',
            name='materia',
            field=models.CharField(max_length=40, null=True),
        ),
    ]
