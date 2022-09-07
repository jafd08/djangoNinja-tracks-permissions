# Generated by Django 4.1 on 2022-09-05 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RightsSupport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'permissions': (('can_add_track', 'User can add track (only superadmin)'),),
                'managed': False,
                'default_permissions': (),
            },
        ),
    ]
