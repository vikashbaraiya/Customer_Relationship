from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()
    join_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_date = models.DateField(auto_now_add=True)
    delivery_date = models.DateField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50)

    def __str__(self):
        return f"Order {self.id} by {self.customer.name}"

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    weight = models.DecimalField(max_digits=6, decimal_places=2)
    dimensions = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Warehouse(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    capacity = models.IntegerField()
    supervisor = models.ForeignKey('Employee', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    hire_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

class Supplier(models.Model):
    name = models.CharField(max_length=100)
    contact_person = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()

    def __str__(self):
        return self.name

class Shipment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    shipment_date = models.DateField()
    shipment_status = models.CharField(max_length=50)
    tracking_number = models.CharField(max_length=50)

    def __str__(self):
        return f"Shipment for Order {self.order.id}"

class Inventory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    quantity_on_hand = models.IntegerField()
    reorder_level = models.IntegerField()
    last_stock_update = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.product.name} in {self.warehouse.name}"

class Transaction(models.Model):
    TRANSACTION_TYPES = [
        ('RECEIVE', 'Receive'),
        ('ISSUE', 'Issue'),
        ('TRANSFER', 'Transfer'),
    ]

    transaction_type = models.CharField(max_length=20, choices=TRANSACTION_TYPES)
    transaction_date = models.DateField()
    quantity = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_transaction_type_display()} of {self.quantity} {self.product.name} at {self.warehouse.name}"
