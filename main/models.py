from django.db import models

# Create your models here.
class stock_directory(models.Model):
    stock_name_in_database=models.CharField(default='',max_length=30)
    stock_symbol_in_database=models.CharField(default='',max_length=30)
    stock_buy_price_in_database=models.DecimalField(default=0,max_digits=10, decimal_places=2)
    stock_current_price_in_database=models.DecimalField(default=0,max_digits=10, decimal_places=2)
    stock_profit_in_database=models.DecimalField(default=0,max_digits=10, decimal_places=2)
    stock_amount_in_database=models.IntegerField()
    stock_created_time_in_database=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return (self.stock_name_in_database)

class mutual_fund_directory(models.Model):
    mutual_fund_name_in_database=models.CharField(default='',max_length=30)
    mutual_fund_type_in_database=models.CharField(default='',max_length=30)
    mutual_fund_created_time_in_database=models.DateTimeField(auto_now_add=True)
    mutual_investment_in_database=models.DecimalField(default=0,max_digits=10, decimal_places=2)
    mutual_fund_return_in_database=models.DecimalField(default=0,max_digits=10, decimal_places=2)
    mutual_fund_profit_in_database=models.DecimalField(default=0,max_digits=10, decimal_places=2)
    def __str__(self):
        return (self.mutual_fund_name_in_database)

class crypto_currency_directory(models.Model):
    crypto_name_in_database=models.CharField(default='',max_length=30)
    crypto_buy_price_in_database=models.DecimalField(default=0,max_digits=10, decimal_places=2)
    crypto_current_price_in_database=models.DecimalField(default=0,max_digits=10, decimal_places=2)
    stock_profit_in_database=models.DecimalField(default=0,max_digits=10, decimal_places=2)
    stock_created_time_in_database=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return (self.crypto_name_in_database)