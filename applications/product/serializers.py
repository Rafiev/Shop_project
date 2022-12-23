from django.db.models import Avg
from rest_framework import serializers

from applications.product.models import Category, Product, Image


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'

    @staticmethod
    def validate_title(title):
        if Category.objects.filter(title=title.lower).exsist():
            raise serializers.ValidationError('Такая категория уже существует')
        return title


class ProductImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    owner = serializers.EmailField(required=False)
    images = ProductImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = '__all__'

    def create(self, validated_data):
        request = self.context.get('request')
        product = Product.objects.create(**validated_data)
        files = request.FILES
        list_images = []
        for image in files.getlist('images'):
            list_images.append(Image(product=product, image=image))
        Image.objects.bulk_create(list_images)
        return product

    def to_representation(self, instance):
        res = super().to_representation(instance)
        res['likes'] = instance.likes.filter(like=True).count()
        res['rating'] = instance.ratings.all().aggregate(Avg('rating'))['rating__avg']
        return res