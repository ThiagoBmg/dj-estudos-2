# Generated by Django 3.2.6 on 2021-08-28 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210828_1210'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='id_pedido')),
                ('name', models.CharField(max_length=100, verbose_name='nome')),
                ('status', models.CharField(max_length=100, verbose_name='status')),
            ],
        ),
    ]