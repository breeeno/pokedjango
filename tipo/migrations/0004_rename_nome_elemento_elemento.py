# Generated by Django 4.0.3 on 2022-03-28 18:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tipo', '0003_elemento_delete_elementos'),
    ]

    operations = [
        migrations.RenameField(
            model_name='elemento',
            old_name='nome',
            new_name='elemento',
        ),
    ]
