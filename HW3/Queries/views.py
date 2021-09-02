from django.db.models.expressions import Value
from django.http.response import JsonResponse
from django.shortcuts import render
from .models import *
from django.http import HttpResponse , JsonResponse
from django.utils import timezone
import datetime
from django.views import generic
from django.db.models import Count , F , Q
# Create your views here.

def all_customers_view(request):
    all_customers = Customer.objects.all().values()
    json_object = {
        "all" : list(all_customers)
    }
    return JsonResponse(json_object)



def last_15_days(request):
    orders =[]
    for o in Order.objects.all():
        now = timezone.now()
        if o.order_time and (now - o.order_time).days == 15:
            orders.append(o)
            print(o)
    orders_count = len(orders) * 0.1
    for item in orders[0:int(orders_count)]:
        print(item)
    return HttpResponse(orders[0:int(orders_count)])


def customers_in_an_specific_period(request):
    ordersquery = Order.objects.filter(order_time__gte = datetime.date(1998 ,1,1),
                                        order_time__lte = datetime.date(2000,1,1))
    customers = []
    for o in ordersquery:
        customers.append(o.customer.user)
    
    for i in range(0 , len(customers)):
        print(customers[i])

    return HttpResponse(customers)


def all_employees_view(request):
    all_employees = Employee.objects.all()
    for item in all_employees:
        print(item)
    return HttpResponse(all_employees)


def each_customer_ordered_products(request):
    customer_ordered_products =  OrderDetail.objects.select_related('product' , 'order__customer')

    return HttpResponse(customer_ordered_products)


def each_product_category(request):
    products_category = Product.objects.all().select_related('category').annotate( pro_cat = F('category__category_name'))
    for c in products_category:
        print(c)
    # *********************************************************************************************************************
    categories = Product.objects.annotate(value=F('product_name') ,category_name=F('category') , label=F('product_name') ).values('category__category_name' , 'value' , 'label' , 'product_name')
    return HttpResponse(categories)


class CatagoryList(generic.ListView):
    template_name = 'product_list.html'
    def get_queryset(self) :
        return Product.objects.all().select_related('category')


def five_customers_with_most_expensive_products(request):
    q = OrderDetail.objects.all().annotate(product_price = F('product__unit_price')).order_by('-product_price')[:5]
    return HttpResponse(q)

def orders_in_june_2007(request):

    june_orders = Order.objects.filter(order_time__year='2021' , order_time__month='09')
    if len(june_orders) == 0:
        return HttpResponse("There is no order in june 2007")
    return HttpResponse(june_orders)

def last_order_in_recent_month(request):
    today = datetime.datetime.now()
    l = Order.objects.filter(order_time__year=today.year, order_time__month=today.month).last()
    return HttpResponse(l)

# filter((F('unit_price') * F('quantity'))__gt = 10000)

def orders_with_more_than_10000_cost(request):
    q = OrderDetail.objects.annotate(total_cost = F('unit_price') * F('quantity') , order_shenase = F('order__pk')).filter(total_cost__gt = 10000).values('total_cost' , 'order_shenase')
    return HttpResponse(q)


def orders_in_12_Feb_2007(request):
    feb_orders = OrderDetail.objects.filter(order__order_time__year = '2021' , 
                                                order__order_time__month = '09',
                                                order__order_time__day = '02').annotate(customer = F('order__customer__user__first_name') , ordered_product = F('product__product_name')).values()

    return HttpResponse(feb_orders)

def customers_did_not_have_order_untill_june(request):
    # ????????????????????
    pass


def yes_no_in_Feb_12_2007(request):
    feb_orders = OrderDetail.objects.filter(order__order_time__year = '2021' , 
                                                order__order_time__month = '09',
                                                order__order_time__day = '02').annotate(customer = F('order__customer__user__first_name') , ordered_product = F('product__product_name')).values()
    #  ?????????????????
    return HttpResponse(feb_orders)





