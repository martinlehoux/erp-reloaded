# Generated by Django 3.0.3 on 2020-03-02 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0008_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='last_name',
            field=models.CharField(blank=True, max_length=256),
        ),
    ]
