# Generated by Django 3.1.4 on 2021-06-05 07:33

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hashtag',
            fields=[
                ('hashtagId', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('hashtagName', models.CharField(max_length=100, unique=True)),
            ],
        ),
    ]
