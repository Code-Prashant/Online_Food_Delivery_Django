# Generated by Django 3.1.3 on 2020-11-07 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzaapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerModal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.CharField(max_length=10)),
                ('phone', models.CharField(max_length=10)),
            ],
        ),
    ]