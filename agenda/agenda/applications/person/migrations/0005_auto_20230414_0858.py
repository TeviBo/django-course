# Generated by Django 3.1 on 2023-04-14 08:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0004_person_hobbies'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='hobby',
            options={'verbose_name': 'Hobby', 'verbose_name_plural': 'Hobbies'},
        ),
    ]
