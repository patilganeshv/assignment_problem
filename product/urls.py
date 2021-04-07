
from django.contrib import admin
from django.urls import path, include
from product import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.product, name='product'),
    path('products', views.products_list, name='products'),
]
