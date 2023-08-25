# Generated by Django 4.2.4 on 2023-08-25 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('company_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('about', models.TextField()),
                ('type', models.CharField(choices=[('Account', 'Account'), ('IT', 'IT'), ('Other', 'Other')], max_length=20)),
                ('added_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
