from django.contrib import admin
from .models import Customer, Order, Product, Warehouse, Employee, Supplier, Shipment, Inventory, Transaction

admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Product)
admin.site.register(Warehouse)
admin.site.register(Employee)
admin.site.register(Supplier)
admin.site.register(Shipment)
admin.site.register(Inventory)
admin.site.register(Transaction)