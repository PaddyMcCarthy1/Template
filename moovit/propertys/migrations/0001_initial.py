# Generated by Django 2.1.1 on 2018-09-23 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publish_date', models.DateTimeField(auto_created=True)),
                ('title', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['-publish_date'],
            },
        ),
    ]
