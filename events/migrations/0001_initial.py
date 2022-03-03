# Generated by Django 4.0.2 on 2022-03-03 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.CharField(max_length=255)),
                ('date', models.DateTimeField()),
                ('description', models.CharField(max_length=255)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
    ]
