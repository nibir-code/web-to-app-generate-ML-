# Generated by Django 3.2.6 on 2021-10-08 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webtoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='buttoninfo',
            name='Button_Number',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]