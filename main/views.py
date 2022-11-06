from django.shortcuts import render,get_object_or_404,redirect
from finnews.client import News ##import news api of cnbc
from main.models import stock_directory,mutual_fund_directory,crypto_currency_directory
import yfinance as yf
from django.contrib import messages
from datetime import date
from django.contrib.auth.decorators import login_required
from user.models import history


def get_current_price(symbol):
    ticker = yf.Ticker(symbol)
    todays_data = ticker.history(period='1d')
    return todays_data['Close'][0]

@login_required
def index(request):
    timeline=[]
    stock_investment_in_view=[]
    stock_return_in_view=[]
    stock_profit_in_view=[]
    mutual_fund_investment_in_view=[]
    mutual_fund_return_in_view=[]
    mutual_fund_profit_in_view=[]
    data=history.objects.all()
    for i in data:
        stock_investment_in_view.append(i.stocks_investment)
        stock_return_in_view.append(i.stocks_return)
        stock_profit_in_view.append(i.stocks_profit)
        mutual_fund_investment_in_view.append(i.mutual_funds_investment)
        mutual_fund_return_in_view.append(i.mutual_funds_return)
        mutual_fund_profit_in_view.append(i.mutual_funds_profit)
        timeline.append(i.data_created_time)
    context={
        'time':timeline,
        'st_investment':stock_investment_in_view,
        'st_return':stock_return_in_view,
        'st_profit':stock_profit_in_view,
        'mf_investment':mutual_fund_investment_in_view,
        'mf_return':mutual_fund_return_in_view,
        'mf_profit':mutual_fund_profit_in_view,
    }
    return render(request,'index.html',context)

def stocks(request):
    all_news=[]
    # Create a new instance of the News Client.
    news_client = News()
    # Grab the CNBC News Client.
    cnbc_news_client = news_client.cnbc
    # Grab the top news.
    cbnc_top_news = cnbc_news_client.news_feed(topic='finance')
    for i in cbnc_top_news:
        all_news.append(i['title'])
    context={'dataline':all_news}
    return render(request,'stocks.html',context)

@login_required
def new_stock(request,*args, **kwargs):
    if request.method=="POST":
        stnm=request.POST.get('stock_name')
        stsy=request.POST.get('stock_symbol')
        stbp=request.POST.get('stock_buy_price')
        stcp=request.POST.get('stock_current_price')
        stam=request.POST.get('stock_amount')
        stpf=((float(stcp))-(float(stbp)))*(float(stam))
        if stock_directory.objects.filter(stock_symbol_in_database=stsy.upper()).exists():
            messages.success(request,("This stock is already exist in the database"))
            return redirect('new_stock')
        data=stock_directory(stock_name_in_database=stnm.upper(),stock_symbol_in_database=stsy.upper(),stock_buy_price_in_database=stbp,stock_current_price_in_database=stcp,stock_profit_in_database=stpf,stock_amount_in_database=stam)
        data.save()
        return render(request,'success.html',{'confirmation':"Your data is submitted successfully"})
    return render(request,'new_stock.html')

@login_required
def stocks_record(request,*args, **kwargs):
    stock_data=stock_directory.objects.all()
    for i in stock_data:
        symbol=i.stock_symbol_in_database+".NS"
        latest_price=get_current_price(symbol)
        i.stock_current_price_in_database=round(latest_price,2)
        i.save()
    return render(request,'stocks_record.html',{'dataline':stock_data})

@login_required
def stock_add(request,pk):
    stock_data=get_object_or_404(stock_directory, pk=pk)
    symbol=stock_data.stock_symbol_in_database+'.NS'
    price_data=round(get_current_price(symbol),2)
    if request.method=="POST":
        new_quantity=request.POST.get('stock_amount')
        new_buy_price=request.POST.get('buy_price')
        current_price=price_data
        old_quantity=stock_data.stock_amount_in_database
        old_buy_price=stock_data.stock_buy_price_in_database
        total_quantity=int(old_quantity)+int(new_quantity)
        Total_buy_price=(float(old_quantity)*float(old_buy_price))+(float(new_quantity)*float(new_buy_price))
        Avarage_buy_price=Total_buy_price/total_quantity
        Profit_amount=(float(current_price)-float(Avarage_buy_price))*total_quantity
        stock_data.stock_buy_price_in_database=round(Avarage_buy_price,2)
        stock_data.stock_current_price_in_database=current_price
        stock_data.stock_profit_in_database=round(Profit_amount,2)
        stock_data.stock_amount_in_database=total_quantity
        stock_data.save()
        return render(request,'success.html',{'confirmation':"Your data is successfully updated in the database"})
    context={
        'dataline':stock_data,
        'price':price_data
    }
    return render(request,'stock_add.html',context)

@login_required
def stock_delete(request,pk):
    data_line = get_object_or_404(stock_directory, pk=pk)
    data_line.delete()
    messages.success(request,("That data is deleted successfully !!"))
    return redirect('stocks_record')

@login_required
def stock_detail(request,pk):
    stock_data=get_object_or_404(stock_directory, pk=pk)
    amount_invested=(float(stock_data.stock_buy_price_in_database)*stock_data.stock_amount_in_database)
    amount_return=(float(stock_data.stock_current_price_in_database)*stock_data.stock_amount_in_database)
    context={
        'dataline':stock_data,
        'investment':round(amount_invested,2),
        'return':round(amount_return,2)
    }
    return render(request,'stock_detail.html',context)

@login_required
def stock_edit(request,pk):
    stock_data=get_object_or_404(stock_directory, pk=pk)
    symbol=stock_data.stock_symbol_in_database+'.NS'
    price_data=round(get_current_price(symbol),2)
    if request.method=="POST":
        stock_name_in_view=request.POST.get("stock_name")
        stock_buy_price_in_view=request.POST.get("buy_price")
        stock_symbol_in_view=request.POST.get("stock_symbol")
        stock_current_price_in_view=price_data
        stock_amount_in_view=request.POST.get("stock_amount")
        stock_profit_in_view=(float(stock_current_price_in_view)-float(stock_buy_price_in_view))*(float(stock_amount_in_view))
        stock_data.stock_name_in_database=stock_name_in_view
        stock_data.stock_symbol_in_database=stock_symbol_in_view
        stock_data.stock_buy_price_in_database=stock_buy_price_in_view
        stock_data.stock_current_price_in_database=stock_current_price_in_view
        stock_data.stock_amount_in_database=stock_amount_in_view
        stock_data.stock_profit_in_database=round(stock_profit_in_view,2)
        stock_data.save()
        return render(request,'success.html',{"confirmation":"Your data is updated successfully"})
    context={
        'dataline':stock_data,
        'today_price':price_data
    }
    return render(request,'stock_edit.html',context)

################################################ stock property ends here ################################################################### 
@login_required
def mutual_fund(request):
    return render(request,'mutual_fund.html')

@login_required
def new_mutual_fund(request):
    if request.method=="POST":
        mfnm=request.POST.get('fund_name')
        mftp=request.POST.get('fund_type')
        mfin=request.POST.get('fund_investment')
        mfrt=request.POST.get('fund_return')
        mfpr=float(mfrt)-float(mfin)
        data=mutual_fund_directory(mutual_fund_name_in_database=mfnm.upper(),mutual_fund_type_in_database=mftp,mutual_investment_in_database=mfin,mutual_fund_return_in_database=mfrt,mutual_fund_profit_in_database=mfpr)
        data.save()
        return render(request,'success.html',{'confirmation':"Your Mutual Fund data saved successfully"})
    return render(request,'new_mutual_fund.html')

@login_required
def mutual_fund_record(request,*args, **kwargs):
    fund_data=mutual_fund_directory.objects.all()
    return render(request,'mutual_fund_record.html',{'dataline':fund_data})

@login_required
def mutual_fund_detail(request,pk):
    fund_data=get_object_or_404(mutual_fund_directory, pk=pk)
    context={
        'dataline':fund_data,
    }
    return render(request,'mutual_fund_detail.html',context)

@login_required
def mutual_fund_delete(request,pk):
    data_line = get_object_or_404(mutual_fund_directory, pk=pk)
    data_line.delete()
    messages.success(request,("That data is deleted successfully !!"))
    return redirect('mutual_fund_record')

@login_required
def mutual_fund_edit(request,pk):
    fund_data=get_object_or_404(mutual_fund_directory, pk=pk)
    if request.method=="POST":
        mf_name_in_view=request.POST.get("fund_name")
        mf_investment_in_view=request.POST.get("investment")
        mf_return_in_view=request.POST.get("current_value")
        mf_profit_in_view=(float(mf_return_in_view)-float(mf_investment_in_view))
        fund_data.mutual_fund_name_in_database=mf_name_in_view
        fund_data.mutual_investment_in_database=mf_investment_in_view
        fund_data.mutual_fund_return_in_database=mf_return_in_view
        fund_data.mutual_fund_profit_in_database=mf_profit_in_view
        fund_data.save()
        return render(request,'success.html',{"confirmation":"Your data is updated successfully"})
    context={
        'dataline':fund_data,
    }
    return render(request,'mutual_fund_edit.html',context)
#############################################  mutual fund property ends here ##############################################################
@login_required
def records(request,*args, **kwargs):
    today_data = date.today()
    dd=today_data.strftime("%B %d, %Y")
    stock_data=stock_directory.objects.all()
    fund_data=mutual_fund_directory.objects.all()
    stock_invetsted=[]
    stock_return=[]
    stock_profit=[]
    fund_invetsted=[]
    fund_return=[]
    fund_profit=[]
    for i in stock_data:
        stock_invetsted.append((float(i.stock_buy_price_in_database)*float(i.stock_amount_in_database)))
        stock_return.append((float(i.stock_current_price_in_database)*float(i.stock_amount_in_database)))
        stock_profit.append(float(i.stock_profit_in_database))
    for i in fund_data:
        fund_invetsted.append(float(i.mutual_investment_in_database))
        fund_return.append(float(i.mutual_investment_in_database))
        fund_profit.append(float(i.mutual_fund_profit_in_database))
    total_investment=sum(stock_invetsted)+sum(fund_invetsted)
    total_return=sum(fund_return)+sum(stock_return)
    total_profit=sum(stock_profit)+sum(fund_profit)
    context={
        'datetime':dd,
        'stockline':stock_data,
        'fundline':fund_data,
        'st_investment':round(sum(stock_invetsted),2),
        'st_return':round(sum(stock_return),2),
        'st_profit':round(sum(stock_profit),2),
        'mf_investment':(sum(fund_invetsted)),
        'mf_return':(sum(fund_return)),
        'mf_profit':(sum(fund_profit)),
        'ttin':total_investment,
        'ttpr':round(total_profit,2),
        'ntwr':total_return
    }
    return render(request,'records.html',context)

def record_history(request):
    stock_data=stock_directory.objects.all()
    fund_data=mutual_fund_directory.objects.all()
    stock_invetsted=[]
    stock_return=[]
    stock_profit=[]
    fund_invetsted=[]
    fund_return=[]
    fund_profit=[]
    for i in stock_data:
        stock_invetsted.append((float(i.stock_buy_price_in_database)*float(i.stock_amount_in_database)))
        stock_return.append((float(i.stock_current_price_in_database)*float(i.stock_amount_in_database)))
        stock_profit.append(float(i.stock_profit_in_database))
    for i in fund_data:
        fund_invetsted.append(float(i.mutual_investment_in_database))
        fund_return.append(float(i.mutual_investment_in_database))
        fund_profit.append(float(i.mutual_fund_profit_in_database))
    total_investment=sum(stock_invetsted)+sum(fund_invetsted)
    total_return=sum(fund_return)+sum(stock_return)
    total_profit=sum(stock_profit)+sum(fund_profit)
    data=history(stocks_investment=sum(stock_invetsted),stocks_return=sum(stock_return),stocks_profit=sum(stock_profit),mutual_funds_investment=sum(fund_invetsted),mutual_funds_return=sum(fund_return),mutual_funds_profit=sum(fund_profit),total_investment=total_investment,total_return=total_return,total_profit=total_profit)
    data.save()
    return render(request,'success.html',{'confirmation':"Your data is saved to database successfully !"})

