# Generated by Django 3.1.5 on 2021-02-06 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0011_auto_20210205_1511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infectedplace',
            name='happened_at',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
