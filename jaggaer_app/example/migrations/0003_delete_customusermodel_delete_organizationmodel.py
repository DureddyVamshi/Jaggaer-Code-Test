# Generated by Django 4.2.3 on 2023-07-11 19:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('example', '0002_organizationmodel'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUserModel',
        ),
        migrations.DeleteModel(
            name='OrganizationModel',
        ),
    ]
