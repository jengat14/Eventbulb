# Generated by Django 4.0.2 on 2022-03-23 18:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_userprofile_attending'),
        ('events', '0007_remove_review_event_id_review_event_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='event',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='events.event'),
        ),
        migrations.AlterField(
            model_name='review',
            name='profile',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='accounts.userprofile'),
        ),
    ]
