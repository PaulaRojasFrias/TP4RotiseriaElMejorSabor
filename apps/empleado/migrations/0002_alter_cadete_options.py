# Generated by Django 4.1.2 on 2022-10-21 23:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empleado', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cadete',
            options={'ordering': ('nombre_completo',)},
        ),
    ]
