# Generated by Django 3.2.18 on 2023-05-25 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_order_initiator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('CREATED', 'Created'), ('PAID', 'Paid'), ('ON_WAY', 'Delivering'), ('DELIVERED', 'Delivered')], default='CREATED', max_length=22),
        ),
    ]
