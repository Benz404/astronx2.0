from django.db import models

# Create your models here.
class history(models.Model):
    data_created_time=models.DateTimeField(auto_now_add=True)
    stocks_investment=models.DecimalField(default=0,max_digits=10, decimal_places=2)
    stocks_return=models.DecimalField(default=0,max_digits=10, decimal_places=2)
    stocks_profit=models.DecimalField(default=0,max_digits=10, decimal_places=2)
    mutual_funds_investment=models.DecimalField(default=0,max_digits=10, decimal_places=2)
    mutual_funds_return=models.DecimalField(default=0,max_digits=10, decimal_places=2)
    mutual_funds_profit=models.DecimalField(default=0,max_digits=10, decimal_places=2)
    total_investment=models.DecimalField(default=0,max_digits=10, decimal_places=2)
    total_return=models.DecimalField(default=0,max_digits=10, decimal_places=2)
    total_profit=models.DecimalField(default=0,max_digits=10, decimal_places=2)
    def __str__(self):
        return str(self.data_created_time)