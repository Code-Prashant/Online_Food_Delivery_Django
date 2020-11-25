from django.contrib import admin
from django.urls import path
from .views import reject_order, accept_order, admin_order, user_order, placed_order, user_logout, userauthenticate, customer_view, user_login_view, home_page_view, admin_login_view, admin_home_page_view, sign_up_user, authenticateadmin, admin_logout, addpizza, delete_pizza

urlpatterns = [
    path('admin/', admin_login_view, name= 'adminloginpage'),
    path('adminauthenticate/', authenticateadmin),
    path('admin/homepage', admin_home_page_view, name= 'adminhomepage'),
    path('adminlogout/', admin_logout),
    path('addpizza/', addpizza),
    path('deletepizza/<int:pizzaid>/', delete_pizza ),
    path('', home_page_view, name= 'homepage'),
    path('signupuser/', sign_up_user),
    path('loginuser/', user_login_view, name= 'userlogin'),
    path('customer/welcome', customer_view, name= 'customerview'),
    path('customer/authenticate', userauthenticate),
    path('userlogout/', user_logout),
    path('placeorder/', placed_order),
    path('userorder/', user_order),
    path('checkorder/', admin_order),
    path('accept/<int:orderpk>/', accept_order),
    path('reject/<int:orderpk>/', reject_order)

]
