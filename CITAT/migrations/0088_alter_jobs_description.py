# Generated by Django 3.2.5 on 2022-04-10 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CITAT', '0087_jobs_company_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobs',
            name='description',
            field=models.TextField(max_length=200, null=True),
        ),
    ]