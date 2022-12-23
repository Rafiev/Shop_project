from rest_framework import serializers

from applications.feedback.models import Comment, Like, Rating, Favourite
from applications.product.models import Product


class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.CharField(required=False)

    class Meta:
        model = Comment
        fields = '__all__'


class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Like
        fields = ['like', 'product']


class RatingSerializer(serializers.ModelSerializer):
    rating = serializers.IntegerField(min_value=1, max_value=5)

    class Meta:
        model = Rating
        fields = ['rating']


class FavouriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Favourite
        fields = '__all__'

    def to_representation(self, instance):
        res = super().to_representation(instance)
        res['product'] = instance.product.title
        return res