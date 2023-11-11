from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import LoginForm, RegisterForm, AddressForm
from .models import Pizza, Order, OrderItem
from django.contrib.auth.decorators import login_required

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
            user = User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password'],first_name=request.POST["first_name"])
            user.save()
            login(request, user)
            return redirect('/')
    context = {"form": form}
    return render(request, "orders/register.html", context)

def menu_view(request, *args, **kwargs):
    pizzas = Pizza.objects.all()
    context = {"pizzas":pizzas}
    return render(request, "orders/menu.html", context)

@login_required
def add_to_cart_view(request, *args, **kwargs):
    pizza_id = request.GET.get('pizza_id','')
    size = request.GET.get('size','')
    active_user_orders = Order.objects.filter(customer=request.user, is_ordered=False)
    if not active_user_orders:
        order = Order(customer=request.user, address="", phone_number=0, is_ordered=False, is_done=False)
        order.save()
        order_item = OrderItem(order=order, pizza=Pizza.objects.get(pk=pizza_id), size=size)
        order_item.save()
    else:
        order = active_user_orders[0]
        order_item = OrderItem(order=order, pizza=Pizza.objects.get(pk=pizza_id), size=size)
        order_item.save()
    return redirect('/menu')

@login_required
def cart_view(request, *args, **kwargs):
    form = AddressForm()
    current_order = Order.objects.filter(customer=request.user, is_ordered=False)
    final_price = 0
    cart = []
    if current_order:
        current_order = current_order[0]
        cart = OrderItem.objects.filter(order=current_order)
        for item in cart:
            if item.size == "M":
                final_price += item.pizza.price_medium_size
            else:
                final_price += item.pizza.price_large_size
        final_price = round(final_price, 2)
    if request.method == "POST":
        form = AddressForm(request.POST)
        if form.is_valid():
            current_order.address = request.POST['address']
            current_order.phone_number = request.POST['phone_number']
            current_order.is_ordered = True
            current_order.save()
            return redirect('/menu')
    context = {
        "cart": cart,
        "final_price": final_price,
        "form": form
            }
    return render(request, "orders/cart.html", context)

def delete_item_view(request, *args, **kwargs):
    order_item_id = request.GET.get('order_item_id','')
    order_item = OrderItem.objects.get(pk=order_item_id)
    if not request.user.is_authenticated:
        return redirect('/')
    if order_item.order.customer.id is not request.user.id:
        return redirect('/')
    if order_item.order.is_ordered:
        return redirect('/')
    order_item.delete()
    return redirect('/cart')