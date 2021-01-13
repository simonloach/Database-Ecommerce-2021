# Generated by Django 3.1.4 on 2021-01-11 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sklep', '0005_authgroup_authgrouppermissions_authpermission_authuser_authusergroups_authuseruserpermissions_catego'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('cart_id', models.IntegerField(primary_key=True, serialize=False)),
                ('pid', models.IntegerField(blank=True, null=True)),
                ('quantity', models.IntegerField()),
            ],
            options={
                'db_table': 'cart',
                'managed': False,
            },
        ),
    ]
