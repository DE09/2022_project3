# Generated by Django 4.1.1 on 2022-10-10 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lohandsoft_register', '0002_delete_position'),
    ]

    operations = [
        migrations.CreateModel(
            name='employee_list',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_id', models.CharField(max_length=10)),
                ('employee_pass', models.CharField(max_length=10)),
            ],
        ),
    ]
