from rest_framework import serializers
from .models import Product
from categories.models import Category
from categories.serializers import CategorySerializer


class ProductSerializer(serializers.ModelSerializer):
    category_details = CategorySerializer(source='category', read_only=True)
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        write_only=True
    )
    
    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'slug', 'category', 
                  'category_details', 'price', 'stock_quantity', 'image',
                  'is_active', 'featured', 'in_stock', 'created_at', 'updated_at')
        read_only_fields = ('id', 'in_stock', 'created_at', 'updated_at')


class ProductListSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    
    class Meta:
        model = Product
        fields = ('id', 'name', 'slug', 'category_name', 'price', 
                  'stock_quantity', 'image', 'in_stock', 'featured')