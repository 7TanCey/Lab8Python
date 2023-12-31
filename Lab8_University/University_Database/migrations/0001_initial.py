# Generated by Django 4.2.7 on 2023-11-16 12:55

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('surname', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=30)),
                ('patronymic', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=10)),
                ('course', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(4)])),
                ('faculty', models.CharField(max_length=50)),
                ('grup', models.CharField(max_length=10)),
                ('headman', models.BooleanField()),
            ],
            options={
                'verbose_name': 'Студент',
                'verbose_name_plural': 'Студенти',
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('hours', models.IntegerField()),
                ('semesters', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Предмет',
                'verbose_name_plural': 'Предмети',
            },
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('grade', models.IntegerField(validators=[django.core.validators.MinValueValidator(2), django.core.validators.MaxValueValidator(5)])),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='University_Database.student')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='University_Database.subject')),
            ],
            options={
                'verbose_name': 'Екзамен',
                'verbose_name_plural': 'Екзамени',
            },
        ),
    ]
