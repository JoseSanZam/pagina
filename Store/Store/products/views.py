from typing import Any
from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Product
from django.views.generic.detail import DetailView

class ProductListView(ListView):
    template_name = 'index.html'
    queryset = Product.objects.all().order_by('-id')



    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['subtitle']='Listado de Productos'
        context['Productos']= context['product_list']
        print(context)
        return context
    
    
    
class ProductDetailView(DetailView):
    model=Product
    template_name='products/product.html'


def ver_detalle(request,pk):
    producto=Product.objects.filter(pk=pk).first()
    return render(request, 'products/product.html',{
        'title': 'description',
        'product': producto
    })
