# Generated by Django 2.2.2 on 2019-07-22 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nduthiApp', '0004_auto_20190722_0945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='insurance',
            name='InsuranceExpiry',
            field=models.DateField(blank=True, max_length=8, null=True),
        ),
    ]
