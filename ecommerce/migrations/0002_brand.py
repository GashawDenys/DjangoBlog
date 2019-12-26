# Generated by Django 2.2.5 on 2019-09-17 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Бренд')),
            ],
            options={
                'verbose_name': 'Бренд',
                'verbose_name_plural': 'Бренди',
                'ordering': ['name'],
            },
        ),
    ]