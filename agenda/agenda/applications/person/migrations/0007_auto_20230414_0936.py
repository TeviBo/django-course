# Generated by Django 3.1 on 2023-04-14 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0006_auto_20230414_0900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hobby',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
