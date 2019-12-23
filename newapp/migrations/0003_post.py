# Generated by Django 3.0.1 on 2019-12-23 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0002_auto_20191223_1722'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('text', models.TextField()),
                ('created_at', models.DateTimeField(editable=False)),
                ('modified_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]