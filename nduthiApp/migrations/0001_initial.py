# Generated by Django 2.2.2 on 2019-07-22 09:18

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='myUser',
            fields=[
                ('userID', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Rider',
            fields=[
                ('Name', models.CharField(max_length=300)),
                ('IDNo', models.IntegerField(primary_key=True, serialize=False)),
                ('DateofBirth', models.DateField(max_length=800)),
                ('Gender', models.CharField(max_length=100)),
                ('CountryCode', models.CharField(max_length=40)),
                ('PhoneNumber', models.IntegerField()),
                ('County', models.CharField(max_length=100)),
                ('SubCounty', models.CharField(max_length=100)),
                ('Ward', models.CharField(max_length=100)),
                ('BaseName', models.CharField(max_length=100)),
                ('YearsOfExperience', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('Name', models.CharField(max_length=300)),
                ('FrameNumber', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('Make', models.CharField(max_length=200)),
                ('RegNumber', models.CharField(max_length=100)),
                ('Ownership', models.CharField(max_length=100)),
                ('IDNo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nduthiApp.Rider')),
            ],
        ),
        migrations.CreateModel(
            name='Sacco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=300)),
                ('Membership', models.CharField(max_length=100)),
                ('SaccoName', models.CharField(blank=True, max_length=4)),
                ('DailyContribution', models.IntegerField()),
                ('IDNo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nduthiApp.Rider')),
            ],
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=300)),
                ('IDNo', models.CharField(blank=True, max_length=200, null=True)),
                ('PhoneNumber', models.IntegerField()),
                ('RegNumber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nduthiApp.Vehicle')),
            ],
        ),
        migrations.CreateModel(
            name='Insurance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=300)),
                ('Registration', models.CharField(max_length=100)),
                ('InsuranceCompany', models.CharField(blank=True, max_length=10)),
                ('InsuranceExpiry', models.DateField(blank=True, max_length=8)),
                ('LicenseNumber', models.CharField(max_length=100)),
                ('IDNo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nduthiApp.Vehicle')),
            ],
        ),
    ]
