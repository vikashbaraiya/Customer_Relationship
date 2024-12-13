from django.urls import path
from .views import (
    CustomerListCreate, CustomerDetail,
    OrderListCreate, OrderDetail,
    ProductListCreate, ProductDetail,
    WarehouseListCreate, WarehouseDetail,
    EmployeeListCreate, EmployeeDetail,
    SupplierListCreate, SupplierDetail,
    ShipmentListCreate, ShipmentDetail,
    InventoryListCreate, InventoryDetail,
    TransactionListCreate, TransactionDetail,
    CustomLoginView, CustomLogoutView
)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from rest_framework_simplejwt.views import TokenBlacklistView


urlpatterns = [

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    path('api/token/blacklist/', TokenBlacklistView.as_view(), name='token_blacklist'),


    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),

    path('customers/', CustomerListCreate.as_view(), name='customer-list-create'),
    path('customers/<int:pk>/', CustomerDetail.as_view(), name='customer-detail'),
    
    path('orders/', OrderListCreate.as_view(), name='order-list-create'),
    path('orders/<int:pk>/', OrderDetail.as_view(), name='order-detail'),
    
    path('products/', ProductListCreate.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductDetail.as_view(), name='product-detail'),
    
    path('warehouses/', WarehouseListCreate.as_view(), name='warehouse-list-create'),
    path('warehouses/<int:pk>/', WarehouseDetail.as_view(), name='warehouse-detail'),
    
    path('employees/', EmployeeListCreate.as_view(), name='employee-list-create'),
    path('employees/<int:pk>/', EmployeeDetail.as_view(), name='employee-detail'),
    
    path('suppliers/', SupplierListCreate.as_view(), name='supplier-list-create'),
    path('suppliers/<int:pk>/', SupplierDetail.as_view(), name='supplier-detail'),
    
    path('shipments/', ShipmentListCreate.as_view(), name='shipment-list-create'),
    path('shipments/<int:pk>/', ShipmentDetail.as_view(), name='shipment-detail'),
    
    path('inventories/', InventoryListCreate.as_view(), name='inventory-list-create'),
    path('inventories/<int:pk>/', InventoryDetail.as_view(), name='inventory-detail'),
    
    path('transactions/', TransactionListCreate.as_view(), name='transaction-list-create'),
    path('transactions/<int:pk>/', TransactionDetail.as_view(), name='transaction-detail'),
]