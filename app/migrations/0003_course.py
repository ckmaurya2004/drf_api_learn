# Generated by Django 4.2.2 on 2023-10-11 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_employee_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('discount', models.IntegerField(default=0)),
                ('author_name', models.CharField(max_length=100)),
                ('duration', models.FloatField()),
            ],
        ),
    ]
