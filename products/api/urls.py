from django.urls import path

from .api import (
    ProductListView,
    ProductDetail,
    ProductCreate
)
urlpatterns = [
    path('list-view/', ProductListView.as_view()),
    path('<uuid:id>/detail-view/<str:slug>/', ProductDetail.as_view()),
    path('add_product/', ProductCreate.as_view()),
]