# Generated by Django 2.2.7 on 2021-02-14 03:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('age', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'db_table': 'STUDENT_INFO',
            },
        ),
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coursename', models.CharField(max_length=40)),
                ('coursefees', models.IntegerField()),
                ('students', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='address.Student')),
            ],
            options={
                'db_table': 'COURSE_INFO',
            },
        ),
    ]
