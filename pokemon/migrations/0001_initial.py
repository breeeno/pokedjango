# Generated by Django 4.0.3 on 2022-03-19 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tipo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('sprite', models.ImageField(blank=True, null=True, upload_to='sprites')),
                ('elementos', models.ManyToManyField(to='tipo.tipo')),
            ],
        ),
    ]
