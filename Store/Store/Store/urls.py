from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from . import views
from products.views import ProductListView
from products.views import ProductDetailView
#from accessories.views import AccessorieDetailView
#from accessories.views import AccessorieListView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", ProductListView.as_view(), name ='index'),
   # path("", AccessorieListView.as_view(), name='accesorio'),
    path('users/login',views.login_view,name='login'),
    path('users/logout', views.logout_view,name='logout'),
    path('users/register', views.register, name="register"),
    path('productos/',include('products.urls')),
    path("info",views.info,name='info'),
    path("services",views.services,name="services"),
    path("sale",views.sale,name="sale"),
    #path('accesorios/',include('accessories.urls')),
    
    

]

if settings.DEBUG :
    urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    