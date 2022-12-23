from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action

from applications.feedback.models import Like, Rating, Favourite
from applications.feedback.serializers import RatingSerializer, FavouriteSerializer


class LikeMixin:
    @action(detail=True, methods=['POST'])
    def post(self, request, pk, *args, **kwargs):
        obj, _ = Like.objects.get_or_create(product_id=pk, owner=request.user)
        obj.like = not obj.like
        obj.save()
        status_ = 'Liked'
        if not obj.like:
            status_ = 'Unliked'
        return Response({'status': status_})


class RatingMixin:
    @action(detail=True, methods=['POST'])
    def post(self, request, pk, *args, **kwargs):
        serializer = RatingSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        obj, _ = Rating.objects.get_or_create(product_id=pk, owner=request.user)
        obj.rating = request.data['rating']
        obj.save()
        return Response(request.data, status=status.HTTP_201_CREATED)


class FavouriteMixin:
    @action(detail=True, methods=['POST'])
    def post(self, request, pk, *args, **kwargs):
        obj, _ = Favourite.objects.get_or_create(product_id=pk, owner=request.user)
        obj.save()
        return Response(status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['GET'])
    def get(self, request, pk=None, *args, **kwargs):
        products = Favourite.objects.filter(owner=request.user)
        products_list = FavouriteSerializer(products, many=True)
        return Response(products_list.data, status=status.HTTP_200_OK)

