from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=15)
    description = models.TextField(null=True, blank=True)
    # slug = models.SlugField(max_length=200, unique=True )


    def __str__(self):
        return f"ID: {self.category_id}, {self.category_name}"

    # def get_absolute_url(self):
    #     return reverse("products:tag_index", kwargs={"slug": self.slug})


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=20)
    mobile_number = models.CharField(max_length=11, unique=True)
    birth_date = models.DateField()
    country = models.CharField(max_length=15)
    city = models.CharField(max_length=15)
    region = models.CharField(max_length=15)
    address = models.TextField(null=True, blank=True)
    postal_code = models.CharField(max_length=10, unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=30)

    def __str__(self):
        return f"ID: {self.company_id}, {self.company_name}"


class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    contact_name = models.CharField(max_length=30, unique=True)
    contact_title = models.CharField(max_length=30, null=True)
    ORDER_STATES = (
        ('YES' , 'yes'),
        ('NO' , 'no'),
    )
    has_ordered_or_not = models.CharField(max_length=10 , null=True , blank=True , choices=ORDER_STATES)
    def __str__(self):
        return f"User {self.user.__str__()} \ {self.has_ordered_or_not} \ {self.company.company_name} company.\n"


class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=30, null=True, blank=True)
    hire_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"ID: {self.employee_id}, {self.user.__str__()} {self.title} {self.user.address}"


class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=40)
    category = models.ForeignKey(Category, related_name="product_categories" , on_delete=models.CASCADE)
    unit_price = models.FloatField()
    Inventory = models.IntegerField(default=100)
    # slug = models.SlugField(unique=True )

    def __str__(self):
        return f"ID: {self.product_id}, {self.product_name}: {self.unit_price}"
    
    # def get_absolute_url(self):
    #     return reverse("products:detail", kwargs={"slug": self.slug})


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    order_time = models.DateTimeField(auto_now_add=True , auto_now=False)

    FREIGHT_CHOICES = (
        ('TR', 'Train'),
        ('AR', 'Airplane'),
        ('CA', 'Car'),
    )
    freight = models.CharField(choices=FREIGHT_CHOICES, max_length=10)

    def __str__(self):
        return f"ID: {self.order_id}, Ordered by: {self.customer.user.__str__()}"


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    unit_price = models.FloatField()
    quantity = models.SmallIntegerField(default=1)

    def __str__(self):
        return f"{self.order.customer.user.__str__()}/{self.product.product_name}:{self.unit_price * self.quantity}"

