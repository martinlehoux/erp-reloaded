# Generated by Django 3.0.3 on 2020-03-01 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0005_auto_20200301_1448'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='value_added_tax',
            field=models.DecimalField(decimal_places=4, default='0.2000', max_digits=5),
        ),
    ]
