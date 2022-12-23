from rest_framework.routers import DefaultRouter
from django.urls import path, include

from applications.feedback.views import CommentAPIView, LikeAPIView, RatingAPIView, FavouriteAPIView

router = DefaultRouter()
router.register('comment', CommentAPIView)
router.register('likes', LikeAPIView)
router.register('ratings', RatingAPIView)
router.register('favourites', FavouriteAPIView)

urlpatterns = [
    path('', include(router.urls))
]