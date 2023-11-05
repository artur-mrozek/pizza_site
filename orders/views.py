from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import LoginForm, RegisterForm
from .models import Pizza, Order, OrderItem

# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, "orders/home.html", {})

def login_view(request, *args, **kwargs):
    if request.user.is_authenticated:
        return redirect("/")
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        user = authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return redirect('/login/')
    context = {"form": form}
    return render(request, "orders/login.html", context)

def logout_view(request, *args, **kwargs):
    logout(request)
    return redirect("/")

def register_view(request, *args, **kwargs):
    if request.user.is_authenticated:
        return redirect("/")
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password'])
            user.save()
            login(request, user)
            return redirect('/')
    context = {"form": form}
    return render(request, "orders/register.html", context)

def menu_view(request, *args, **kwargs):
    pizzas = Pizza.objects.all()
    context = {"pizzas":pizzas}
    return render(request, "orders/menu.html", context)

def add_to_cart_view(request, *args, **kwargs):
    pizza_id = request.GET.get('pizza_id','')
    size = request.GET.get('size','')
    active_user_orders = Order.objects.filter(customer=request.user, is_ordered=False)
    if not active_user_orders:
        order = Order(customer=request.user, address="", is_ordered=False, is_done=False)
        order.save()
        order_item = OrderItem(order=order, pizza=Pizza.objects.get(pk=pizza_id), size=size)
        order_item.save()
    else:
        order = active_user_orders[0]
        order_item = OrderItem(order=order, pizza=Pizza.objects.get(pk=pizza_id), size=size)
        order_item.save()
    return redirect('/menu')