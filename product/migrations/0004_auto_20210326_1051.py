# Generated by Django 2.0 on 2021-03-26 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20210326_1044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Volume',
            field=models.IntegerField(blank=True, editable=False),
        ),
    ]
