# Generated by Django 2.2.5 on 2019-09-22 18:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ecommerce', '0008_auto_20190919_2125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='total_price',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=9, verbose_name='Сума'),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name="Ім'я")),
                ('surname', models.CharField(max_length=200, verbose_name='Прізвище')),
                ('phone', models.CharField(max_length=20, verbose_name='Телефон')),
                ('address', models.CharField(max_length=255, verbose_name='Адреса')),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Ціна')),
                ('delivery_type', models.CharField(choices=[('Самовивіз', 'Самовивіз'), ('Доставка', 'Доставка')], max_length=100)),
                ('comment', models.TextField(verbose_name='Коментар')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата')),
                ('status', models.CharField(choices=[('Обробляється', 'Обробляється'), ('Виконується', 'Виконується'), ('Оплачено', 'Оплачено')], max_length=100)),
                ('items', models.ManyToManyField(to='ecommerce.Cart', verbose_name='Товари')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Користувач')),
            ],
        ),
    ]