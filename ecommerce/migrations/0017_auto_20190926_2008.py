# Generated by Django 2.2.5 on 2019-09-26 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0016_auto_20190926_1945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Адреса'),
        ),
        migrations.AlterField(
            model_name='order',
            name='comment',
            field=models.TextField(blank=True, null=True, verbose_name='Коментар'),
        ),
    ]
