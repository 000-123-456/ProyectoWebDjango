# Generated by Django 2.2.3 on 2023-07-25 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0002_alter_servicios_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicios',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
