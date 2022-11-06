from django.contrib import admin
from main.models import stock_directory,mutual_fund_directory,crypto_currency_directory
# Register your models here.
admin.site.register(stock_directory)
admin.site.register(mutual_fund_directory)
admin.site.register(crypto_currency_directory)