from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('Customer', CustomersViewSets, basename='Customer')
router.register('Product', ProductsViewSets, basename='Product')
router.register('Orders', OrdersViewSets, basename='Orders')
router.register('Reviews', ReviewsViewSets, basename='Reviews')


urlpatterns = [
  path('viewset/', include(router.urls)),
  path('viewset/<int:pk>/', include(router.urls)),


]