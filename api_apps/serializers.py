from rest_framework import serializers
from main.models import Category, Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields =['id',
                 'image', 
                 'name',  
                 'price', 
                 'category', 
                 'created_at']