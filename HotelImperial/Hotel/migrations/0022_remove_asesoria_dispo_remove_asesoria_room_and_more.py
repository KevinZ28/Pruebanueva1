# Generated by Django 4.0.5 on 2022-08-24 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hotel', '0021_alter_room_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='asesoria',
            name='dispo',
        ),
        migrations.RemoveField(
            model_name='asesoria',
            name='room',
        ),
        migrations.AddField(
            model_name='asesoria',
            name='state',
            field=models.CharField(default=1, max_length=100, verbose_name='Estado'),
            preserve_default=False,
        ),
    ]
