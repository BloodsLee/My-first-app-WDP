# Generated by Django 4.0.4 on 2022-05-31 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Players', '0003_player_photo_alter_player_next_match_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='photo',
        ),
        migrations.AlterField(
            model_name='player',
            name='next_match_url',
            field=models.CharField(default='https://www.twitch.tv/rainbow6', max_length=255),
        ),
    ]