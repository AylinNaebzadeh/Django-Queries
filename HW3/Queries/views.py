from django.http.response import JsonResponse
from django.shortcuts import render
from .models import *
from django.http import HttpResponse , JsonResponse
from django.utils import timezone
import datetime
from django.views import generic
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
    customer_ordered_products =  OrderDetail.objects.filter(order__customer__user__first_name = 'Aylin')
    return HttpResponse(customer_ordered_products)


class CatagoryList(generic.ListView):
    template_name = 'product_list.html'
    def get_queryset(self) :
        return Product.objects.all().select_related('category')

# https://stackoverflow.com/questions/6436937/query-for-top-x-elements-in-django
# https://stackoverflow.com/questions/5123839/fastest-way-to-get-the-first-object-from-a-queryset-in-django

# last_ten = Messages.objects.filter(since=since).order_by('-id')[:10]
# last_ten_in_ascending_order = reversed(last_ten)
def customers_with_most_expensive_products(request):
    pass





