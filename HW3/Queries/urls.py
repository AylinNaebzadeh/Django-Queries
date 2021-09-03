from django.urls import path , include
from .views import *


app_name = 'Queries'

urlpatterns = [
    path('allcustomers/' , all_customers_view),
    path('allemployees/' , all_employees_view),
    path('last15days/' , last_15_days),
    path('customersincertainperiod/' , customers_in_an_specific_period),
    path('eachcustomerorderedproducts/' , each_customer_ordered_products),
    path('tagsandproducts/' , CatagoryList.as_view()),
    path('eachproductscategory/',each_product_category),
    path('fivemostexpensive/' , five_customers_with_most_expensive_products),
    path('juneorders/' , orders_in_june_2007),
    path('lastorderincurmonth/' , last_order_in_recent_month),
    path('morehtan10000/' , orders_with_more_than_10000_cost),
    path('feborderd/' , orders_in_12_Feb_2007),
    path('morethanaverage/', customers_with_cost_more_than_average),
    path('untilljune/' , customers_did_not_have_order_untill_june),
    path('discount/' , discount),
]
