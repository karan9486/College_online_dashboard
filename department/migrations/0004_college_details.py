# Generated by Django 3.2.3 on 2021-05-23 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0003_auto_20210523_1302'),
    ]

    operations = [
        migrations.CreateModel(
            name='College_Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('college_name', models.CharField(max_length=600)),
                ('college_quote', models.CharField(max_length=800)),
                ('principal_name', models.CharField(max_length=150)),
            ],
        ),
    ]
