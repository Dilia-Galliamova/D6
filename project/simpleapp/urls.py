from django.urls import path
from .views import ProductsList, ProductDetail

urlpatterns = [
   path('', ProductsList.as_view()),
   # pk — это первичный ключ товара, который будет выводиться у нас в шаблон
   # int — указывает на то, что принимаются только целочисленные значения
   path('<int:pk>', ProductDetail.as_view()),
]
