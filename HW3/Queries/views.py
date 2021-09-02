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


def each_post_category(request):
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







