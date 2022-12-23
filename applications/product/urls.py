from rest_framework.routers import DefaultRouter
from applications.product.views import ProductAPIView, CategoryAPIView
from django.urls import path, include

router = DefaultRouter()
router.register('category', CategoryAPIView)
router.register('', ProductAPIView)

urlpatterns = [
    path('', include(router.urls)),
]