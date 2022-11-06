# Generated by Django 4.1.2 on 2022-10-31 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='crypto_currency_directory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crypto_name_in_database', models.CharField(default='', max_length=30)),
                ('crypto_buy_price_in_database', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('crypto_current_price_in_database', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('stock_profit_in_database', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('stock_created_time_in_database', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='mutual_fund_directory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mutual_fund_name_in_database', models.CharField(default='', max_length=30)),
                ('mutual_fund_created_time_in_database', models.DateTimeField(auto_now_add=True)),
                ('mutual_investment_in_database', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('mutual_fund_return_in_database', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('mutual_fund_profit_in_database', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
            ],
        ),
        migrations.AlterField(
            model_name='stock_directory',
            name='stock_buy_price_in_database',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
