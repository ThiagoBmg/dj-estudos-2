# Generated by Django 3.2.6 on 2021-08-28 17:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_pedido'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pedido',
            old_name='name',
            new_name='nome',
        ),
    ]