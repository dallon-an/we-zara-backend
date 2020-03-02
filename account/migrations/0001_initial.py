# Generated by Django 3.0.3 on 2020-03-02 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=500)),
                ('name', models.CharField(max_length=30)),
                ('zip_code', models.CharField(max_length=10)),
                ('address_1', models.CharField(max_length=200)),
                ('address_2', models.CharField(max_length=100, null=True)),
                ('country', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=15)),
                ('upper_body', models.CharField(max_length=10, null=True)),
                ('lower_body', models.CharField(max_length=10, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'accounts',
            },
        ),
    ]
