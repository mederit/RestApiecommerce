# Generated by Django 3.1.7 on 2021-03-16 21:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0003_order_orderitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='order',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='user',
        ),
        migrations.RenameField(
            model_name='cart',
            old_name='user',
            new_name='client',
        ),
        migrations.RenameField(
            model_name='cartitem',
            old_name='user',
            new_name='client',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='OrderItem',
        ),
    ]
