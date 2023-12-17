from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import *


class CustomersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['customer_id', 'first_name', 'last_name']

    def validate(self, attrs):
        unknown = set(self.initial_data) - set(self.fields)
        if unknown:
            raise ValidationError("Unknown field(s): {}".format(", ".join(unknown)))
        return attrs


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price']

    def validate(self, attrs):
        unknown = set(self.initial_data) - set(self.fields)
        if unknown:
            raise ValidationError("Unknown field(s): {}".format(", ".join(unknown)))
        return attrs


class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'customerID', 'productID', 'quantity', 'created_at']

    def validate(self, attrs):
        unknown = set(self.initial_data) - set(self.fields)
        if unknown:
            raise ValidationError("Unknown field(s): {}".format(", ".join(unknown)))
        return attrs


class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'customerID', 'productID', 'rating', 'review']

    def validate(self, attrs):
        unknown = set(self.initial_data) - set(self.fields)
        if unknown:
            raise ValidationError("Unknown field(s): {}".format(", ".join(unknown)))
        return attrs
