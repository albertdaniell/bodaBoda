# Generated by Django 2.2.2 on 2019-07-22 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nduthiApp', '0007_insurance_hasinsurance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sacco',
            name='DailyContribution',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sacco',
            name='SaccoName',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
    ]
