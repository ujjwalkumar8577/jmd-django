# Generated by Django 3.1.4 on 2021-01-07 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shopname', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=12)),
                ('i1', models.FloatField()),
                ('i2', models.FloatField()),
                ('i3', models.FloatField()),
                ('i4', models.FloatField()),
                ('i5', models.FloatField()),
                ('message', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(max_length=12),
        ),
    ]
