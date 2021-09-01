from django.urls import path , include
from .views import *


app_name = 'Queries'

urlpatterns = [
    path('allcustomers/' , all_customers_view),
    path('allemployees/' , all_employees_view),
    path('last15days/' , last_15_days),
    path('customersincertainperiod/' , customers_in_an_specific_period),
]
