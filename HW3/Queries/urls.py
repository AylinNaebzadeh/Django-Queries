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
    path('eachproductscategory/',each_post_category),
    path('fivemostexpensive/' , five_customers_with_most_expensive_products),
]
