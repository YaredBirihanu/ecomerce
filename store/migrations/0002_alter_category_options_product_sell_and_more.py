# Generated by Django 5.1 on 2025-03-08 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'categories'},
        ),
        migrations.AddField(
            model_name='product',
            name='sell',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='sell_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
    ]
