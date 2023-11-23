from django.urls import path
from . import views

urlpatterns=[
    path('<slug:slug>',views.ProductDetailView.as_view(), name='product'),
    path('ver/<int:pk>',views.ver_detalle,name="ver_detalle")
]