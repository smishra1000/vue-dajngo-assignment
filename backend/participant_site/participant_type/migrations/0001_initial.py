# Generated by Django 3.1.1 on 2020-09-05 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ParticipantType',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('participant_type', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'master_participant_type',
                'managed': False,
            },
        ),
    ]