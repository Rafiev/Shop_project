from rest_framework.routers import DefaultRouter
from django.urls import path, include
from applications.order.views import OrderAPIView, OrderConfirmAPIView

router = DefaultRouter()
router.register('', OrderAPIView)

urlpatterns = [
    path('confirm/<uuid:code>/', OrderConfirmAPIView.as_view()),
    path('', include(router.urls))
]