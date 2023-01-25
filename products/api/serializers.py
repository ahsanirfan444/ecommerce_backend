from rest_framework import serializers

from products.models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'id',
            'title',
            'slug',
            'price',
            'description',
            'instock',
            'width_field',
            'height_field',
            'image',
        )
    
    def validate_title(self, data):
        product = Product.objects.filter(title = data).exists()
        if product:
            raise serializers.ValidationError("This product is already exists")
        return data