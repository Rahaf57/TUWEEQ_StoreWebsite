from .models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class CustomersViewSets(viewsets.ModelViewSet):
    serializer_class = CustomersSerializer
    queryset = Customer.objects.all()
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    #authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


class ProductsViewSets(viewsets.ModelViewSet):
    serializer_class = ProductsSerializer
    queryset = Product.objects.all()
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    # authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


class OrdersViewSets(viewsets.ModelViewSet):
    serializer_class = OrdersSerializer
    queryset = Order.objects.all()
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    # authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


class ReviewsViewSets(viewsets.ModelViewSet):
    serializer_class = ReviewsSerializer
    queryset = Review.objects.all()
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    # authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
