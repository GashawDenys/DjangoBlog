# Generated by Django 2.2.5 on 2019-09-19 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0007_cart_cartitem'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cart',
            options={'verbose_name': 'Кошик', 'verbose_name_plural': 'Кошики'},
        ),
        migrations.AlterField(
            model_name='cart',
            name='items',
            field=models.ManyToManyField(blank=True, to='ecommerce.CartItem', verbose_name='Товари'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='total_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=9, verbose_name='Сума'),
        ),
    ]
