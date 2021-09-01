from django.http.response import JsonResponse
from django.shortcuts import render
from .models import *
from django.http import HttpResponse , JsonResponse
from django.utils import timezone
import datetime
# Create your views here.

def all_customers_view(request):
    all_customers = Customer.objects.all().values()
    json_object = {
        "all" : list(all_customers)
    }
    return JsonResponse(json_object)

# d1 = datetime.strptime(self.current_date, "%Y-%m-%d")
# d2 = datetime.strptime(self.dob, "%Y-%m-%d")

# current_age = (d1 - d2).year


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


# گزارشی تهیه کنید که اطلاعات مربوط به مشتریانی را که در یک بازه زمانی مشخص (مثلا 1998-01-01 تا 2000-01-01) خرید داشته‌اند، نمایش دهد.
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



