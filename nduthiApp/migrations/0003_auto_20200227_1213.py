# Generated by Django 2.2 on 2020-02-27 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nduthiApp', '0002_auto_20190820_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='insurance',
            name='InsuranceCompany',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
