# Generated by Django 4.0.2 on 2022-03-23 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0008_alter_review_event_alter_review_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='image',
            field=models.ImageField(blank=True, upload_to='uploads/'),
        ),
    ]
