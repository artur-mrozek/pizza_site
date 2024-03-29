from django.urls import path

from .views import home_view, login_view, logout_view, register_view, menu_view, add_to_cart_view, cart_view, delete_item_view, orders_view, staff_panel_view, make_order_done_view

app_name = "orders"
urlpatterns = [
    path('', home_view, name="home"),
    path('login/', login_view, name="login"),
    path('logout/', logout_view, name="logout"),
    path('register/', register_view, name="register"),
    path('menu/', menu_view, name="menu"),
    path('add_to_cart/', add_to_cart_view, name="add_to_cart"),
    path('cart/', cart_view, name="cart"),
    path('delete_item/', delete_item_view, name="delete_item"),
    path('orders/', orders_view, name="orders"),
    path('staff_panel/', staff_panel_view, name="staff_panel"),
    path('make_order_done/', make_order_done_view, name="make_order_done"),
]