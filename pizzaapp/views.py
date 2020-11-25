from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .models import PizzaModel, CustomerModal, OrderdModel

def admin_login_view(request):
	return render(request, 'pizzaapp/adminlogin.html')

def authenticateadmin(request):
	username = request.POST['username']
	password = request.POST['password']

	user = authenticate(username= username, password= password)
	if user is not None:
		login(request,  user)
		return redirect('adminhomepage')

	if user is None:
		messages.add_message(request, messages.ERROR, "Invalid Credentials")
		return redirect('adminloginpage')

def admin_home_page_view(request):
	if not request.user.is_authenticated:
		return redirect('userlogin')

	context = {
		'pizzas': PizzaModel.objects.all()
	}
	return render(request, 'pizzaapp/adminloginhomepage.html', context)

def admin_logout(request):
	logout(request)
	return redirect('adminloginpage')

def addpizza(request):
	name = request.POST['pizza']
	price = request.POST['price']
	PizzaModel(name= name, price= price).save()
	return redirect('adminhomepage')


def delete_pizza(request, pizzaid):
	PizzaModel.objects.filter(id = pizzaid).delete()
	return redirect('adminhomepage')

def home_page_view(request):
	return render(request, "pizzaapp/homepage.html")

def sign_up_user(request):
	username = request.POST['username']
	password = request.POST['password']
	phone = request.POST['phone']

	#if user is already exist
	if User.objects.filter(username = username).exists():
		messages.add_message(request, messages.ERROR,'USER ALREADY EXIST!!!!')
		return redirect('homepage')
	
	#if user is not exist
	User.objects.create_user(username = username, password = password)
	lastobject = len(User.objects.all()) - 1
	CustomerModal(userid = User.objects.all()[int(lastobject)].id, phone = phone).save()
	messages.add_message(request, messages.SUCCESS,'USER CREATED SUCCESSFULLY!!!!')
	return redirect('homepage')

def user_login_view(request):
	return render(request, 'pizzaapp/userlogin.html')

def userauthenticate(request):
	username = request.POST['username']
	password = request.POST['password']

	user = authenticate(username= username, password= password)
	if user is not None:
		login(request,  user)
		return redirect('customerview')

	if user is None:
		messages.add_message(request, messages.ERROR, "Invalid Credentials")
		return redirect('userlogin')

def customer_view(request):
	if not request.user.is_authenticated:
		return redirect('userlogin')

	username = request.user.username
	context = {
	'username': username, 'pizzas': PizzaModel.objects.all()
	}
	return render(request, 'pizzaapp/customerhomepage.html', context)

def user_logout(request):
	logout(request)
	return redirect('userlogin')

def placed_order(request):
	if not request.user.is_authenticated:
		return redirect('userlogin')

	username = request.user.username
	phone = CustomerModal.objects.filter(userid = request.user.id).first().phone
	address = request.POST['address']
	ordereditem = ""
	for pizza in PizzaModel.objects.all():
		pizzaid = pizza.id
		name = pizza.name
		price = pizza.price

		quantity = request.POST.get(str(pizzaid)," ")
		if str(quantity)!=0 and str(quantity)!=" ":
			ordereditem = ordereditem + name+" " + "price: " + str(int(quantity)*int(price)) +" "+ "quantity: "+ quantity+ " "
	print(ordereditem)

	OrderdModel(username= username, phone= phone, address= address, ordereditem= ordereditem).save()
	messages.add_message(request, messages.ERROR, 'Your Order Successfully placed')
	return redirect('customerview')

def user_order(request):
	orders = OrderdModel.objects.filter(username = request.user.username)
	context = {'orders': orders}
	return render(request, 'pizzaapp/userorder.html', context)

def admin_order(request):
	orders = OrderdModel.objects.all()
	context = {'orders': orders}
	return render(request, 'pizzaapp/checkorder.html', context)

def accept_order(request, orderpk):
	order = OrderdModel.objects.filter(id = orderpk)[0]
	order.status = "Accepted"
	order.save()
	return redirect(request.META['HTTP_REFERER'])

def reject_order(request, orderpk):
	order = OrderdModel.objects.filter(id = orderpk)[0]
	order.status = "Rejected"
	order.save()
	return redirect(request.META['HTTP_REFERER'])