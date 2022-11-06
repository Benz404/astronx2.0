from django.urls import path
from main import views

urlpatterns = [
    path('',views.index,name='index'),
    path('stocks',views.stocks,name='stocks'),
    path('new_stock',views.new_stock,name='new_stock'),
    path('stocks_record',views.stocks_record,name='stocks_record'),
    path('stocks_add/<int:pk>',views.stock_add,name='stock_add'),
    path('stocks_edit/<int:pk>',views.stock_edit,name='stock_edit'),
    path('stocks_detail/<int:pk>',views.stock_detail,name='stock_detail'),
    path('stock_delete/<int:pk>', views.stock_delete ,name='stock_delete'),
    ############### stocks url ends here ###########################
    path('mutual_fund',views.mutual_fund,name='mutual_fund'),
    path('new_mutual_fund',views.new_mutual_fund,name='new_mutual_fund'),
    path('mutual_fund_record',views.mutual_fund_record,name='mutual_fund_record'),
    path('mutual_fund_edit/<int:pk>',views.mutual_fund_edit,name='mutual_fund_edit'),
    path('mutual_fund_detail/<int:pk>',views.mutual_fund_detail,name='mutual_fund_detail'),
    path('mutual_fund_delete/<int:pk>', views.mutual_fund_delete ,name='mutual_fund_delete'),
    ################################################################
    path('records',views.records,name='records'),
    path('record_history',views.record_history,name='record_history'),
]
