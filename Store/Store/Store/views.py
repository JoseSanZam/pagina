from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import login, authenticate,logout
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import registerForm
from products.models import Product
#from accessories.models import Accesorie


def index(request):
    products = Product.objects.all().order_by('-id')
    return render(request, "index.html",{
    'message' : "mensaje desde views",
    'subtitle' : "Subtitulo Hello",
    'Productos' : products,

    })


def login_view(request):
    if request.user.is_authenticated:
        return redirect('index') 
    
    if request.method=='POST':
        username_in = request.POST.get('username')
        password_in =request.POST.get('password')
        user =authenticate(username= username_in, password =password_in)

        if user:
                login(request, user)
                messages.success(request, 'Bienvenido')
                return redirect('index')
    
        else: 
            messages.error(request,'Usuario invalido')
 
    return render(request, 'users/login.html',{})

def logout_view(request):

    logout(request)
    messages.info(request, "Sesión cerrada")
    return (redirect("login"))

def register(request):
    if request.user.is_authenticated:
        return redirect('index')
    form = registerForm(request.POST or None)


    if request.method == 'POST' and form.is_valid():
        user = form.save()

        if user:
            login(request, user)
            messages.success(request,'Usuario registrado exitosamente')
            return redirect('index')
    return render(request, "users/register.html",{'form':form})

def info(request):
    return render(request,'info.html')

def services(request):
    return render(request,'services.html')

def sale (request):
    return render(request,'sale.html')

#def accesories (request):
    accesories=Accesorie.objects.all().order_by('-id')

    return render (request, "index.html",{
    'message' : "mensaje desde views",
    'subtitle' : "Subtitulo Hello",
    'Accesorios' : accesories,
    })