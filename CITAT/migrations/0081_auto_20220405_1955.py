# Generated by Django 3.1.7 on 2022-04-05 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CITAT', '0080_auto_20220405_1801'),
    ]

    operations = [
        migrations.AddField(
            model_name='companyphoto',
            name='firstname',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='companyphoto',
            name='lastname',
            field=models.CharField(max_length=200, null=True),
        ),
    ]