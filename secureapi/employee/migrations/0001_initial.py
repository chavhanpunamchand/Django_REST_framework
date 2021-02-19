# Generated by Django 2.2.7 on 2021-02-13 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('age', models.IntegerField()),
                ('role', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'EMP_INFO',
            },
        ),
    ]