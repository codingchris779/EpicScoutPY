# Generated by Django 2.2.2 on 2019-06-23 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scout', '0002_info_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='TeamNum',
            field=models.CharField(default='null', max_length=200),
            preserve_default=False,
        ),
    ]