# Generated by Django 3.1.4 on 2021-06-05 07:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('UserProfiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserSetting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profileStatus', models.IntegerField(default=0)),
                ('profileType', models.IntegerField(default=0)),
                ('protected', models.IntegerField(default=0)),
                ('userProfile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='UserProfiles.userprofile')),
            ],
        ),
    ]
