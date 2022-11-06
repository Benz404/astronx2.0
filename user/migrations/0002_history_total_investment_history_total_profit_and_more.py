# Generated by Django 4.1.2 on 2022-11-03 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='history',
            name='total_investment',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='history',
            name='total_profit',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='history',
            name='total_return',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]