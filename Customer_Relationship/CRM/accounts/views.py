from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Customer, Order, Product, Warehouse, Employee, Supplier, Shipment, Inventory, Transaction
from .serializers import CustomerSerializer, OrderSerializer, ProductSerializer, WarehouseSerializer, EmployeeSerializer, SupplierSerializer, ShipmentSerializer, InventorySerializer, TransactionSerializer
from .permissions import IsManager, IsAdminUser
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login, logout
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.authentication import JWTAuthentication




class CustomLoginView(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        
        # Authenticate user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            
            # Create JWT tokens
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            refresh_token = str(refresh)
            
            return Response({
                'access': access_token,
                'refresh': refresh_token
            }, status=status.HTTP_200_OK)
        
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class CustomLogoutView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.data.get('refresh')
            token = RefreshToken(refresh_token)
            token.blacklist()  # This will add the token to the blacklist
            return Response({'message': 'Logged out successfully'}, status=status.HTTP_200_OK)
        except TokenError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class CustomerListCreate(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    def get(self, request, format=None):
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CustomerDetail(APIView):
    permission_classes = [IsAdminUser]

    def get_object(self, pk):
        try:
            return Customer.objects.get(pk=pk)
        except Customer.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        customer = self.get_object(pk)
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        customer = self.get_object(pk)
        serializer = CustomerSerializer(customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        customer = self.get_object(pk)
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class OrderListCreate(APIView):
    permission_classes = [IsManager | IsAdminUser]

    def get(self, request, format=None):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OrderDetail(APIView):
    permission_classes = [IsManager | IsAdminUser]

    def get_object(self, pk):
        try:
            return Order.objects.get(pk=pk)
        except Order.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        order = self.get_object(pk)
        serializer = OrderSerializer(order)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        order = self.get_object(pk)
        serializer = OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        order = self.get_object(pk)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ProductListCreate(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request, format=None):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductDetail(APIView):
    permission_classes = [IsAdminUser]

    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        product = self.get_object(pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class WarehouseListCreate(APIView):
    permission_classes = [IsManager | IsAdminUser]

    def get(self, request, format=None):
        warehouses = Warehouse.objects.all()
        serializer = WarehouseSerializer(warehouses, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = WarehouseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class WarehouseDetail(APIView):
    permission_classes = [IsManager | IsAdminUser]

    def get_object(self, pk):
        try:
            return Warehouse.objects.get(pk=pk)
        except Warehouse.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        warehouse = self.get_object(pk)
        serializer = WarehouseSerializer(warehouse)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        warehouse = self.get_object(pk)
        serializer = WarehouseSerializer(warehouse, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        warehouse = self.get_object(pk)
        warehouse.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class EmployeeListCreate(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request, format=None):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EmployeeDetail(APIView):
    permission_classes = [IsAdminUser]

    def get_object(self, pk):
        try:
            return Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        employee = self.get_object(pk)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        employee = self.get_object(pk)
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        employee = self.get_object(pk)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class SupplierListCreate(APIView):
    permission_classes = [IsManager | IsAdminUser]

    def get(self, request, format=None):
        suppliers = Supplier.objects.all()
        serializer = SupplierSerializer(suppliers, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SupplierSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SupplierDetail(APIView):
    permission_classes = [IsManager | IsAdminUser]

    def get_object(self, pk):
        try:
            return Supplier.objects.get(pk=pk)
        except Supplier.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        supplier = self.get_object(pk)
        serializer = SupplierSerializer(supplier)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        supplier = self.get_object(pk)
        serializer = SupplierSerializer(supplier, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        supplier = self.get_object(pk)
        supplier.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ShipmentListCreate(APIView):
    permission_classes = [IsManager | IsAdminUser]

    def get(self, request, format=None):
        shipments = Shipment.objects.all()
        serializer = ShipmentSerializer(shipments, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ShipmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ShipmentDetail(APIView):
    permission_classes = [IsManager | IsAdminUser]

    def get_object(self, pk):
        try:
            return Shipment.objects.get(pk=pk)
        except Shipment.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        shipment = self.get_object(pk)
        serializer = ShipmentSerializer(shipment)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        shipment = self.get_object(pk)
        serializer = ShipmentSerializer(shipment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        shipment = self.get_object(pk)
        shipment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class InventoryListCreate(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request, format=None):
        inventories = Inventory.objects.all()
        serializer = InventorySerializer(inventories, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = InventorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class InventoryDetail(APIView):
    permission_classes = [IsAdminUser]

    def get_object(self, pk):
        try:
            return Inventory.objects.get(pk=pk)
        except Inventory.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        inventory = self.get_object(pk)
        serializer = InventorySerializer(inventory)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        inventory = self.get_object(pk)
        serializer = InventorySerializer(inventory, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        inventory = self.get_object(pk)
        inventory.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class TransactionListCreate(APIView):
    permission_classes = [IsManager | IsAdminUser]

    def get(self, request, format=None):
        transactions = Transaction.objects.all()
        serializer = TransactionSerializer(transactions, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TransactionDetail(APIView):
    permission_classes = [IsManager | IsAdminUser]

    def get_object(self, pk):
        try:
            return Transaction.objects.get(pk=pk)
        except Transaction.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        transaction = self.get_object(pk)
        serializer = TransactionSerializer(transaction)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        transaction = self.get_object(pk)
        serializer = TransactionSerializer(transaction, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        transaction = self.get_object(pk)
        transaction.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)