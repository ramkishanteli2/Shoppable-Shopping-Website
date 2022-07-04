from django.shortcuts import render, redirect
from django.views import View
from .models import Customer, Product, OrderPlaced, Cart, Address
from .forms import CustomerRegistrationForm, CustomerLoginForm, SetNewPassword
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.db.models import Q
from datetime import datetime
from django.contrib.auth.models import User, AbstractUser
from django.urls import reverse
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

# def index(request):
#     return render(request,'app/index.html')
STATE_CHOICES = (
    'Andhra Pradesh',
    'Arunachal Pradesh',
    'Assam',
    'Bihar',
    'Chhattisgarh',
    'Delhi',
    'Goa',
    'Gujarat',
    'Haryana',
    'Himachal Pradesh',
    'J&K',
    'Jharkhand',
    'Karnataka',
    'Kerala',
    'Madhya Pradesh',
    'Maharashtra',
    'Manipur',
    'Meghalaya',
    'Mizoram',
    'Nagaland',
    'Odisha',
    'Punjab',
    'Rajasthan',
    'Sikkim',
    'Tamil Nadu',
    'Telangana',
    'Tripura',
    'Uttar Pradesh',
    'Uttarakhand',
    'West Bengal',
)


class ProductView(View):
    def get(self, request):
        mobiles = Product.objects.filter(category="M")
        topwears = Product.objects.filter(category="TW")
        bottomwears = Product.objects.filter(category="BW")
        if request.user.is_authenticated:
            return render(request, 'app/index.html', {'mobiles': mobiles, 'topwears': topwears, 'bottomwears': bottomwears, 'cart_item_count': Cart.objects.filter(user=request.user).count()})
        else:
            return render(request, 'app/index.html', {'mobiles': mobiles, 'topwears': topwears, 'bottomwears': bottomwears})


def mobile(request, brand_name=None):
    if brand_name == None:
        brand_name = Product.objects.filter(category="M")
    elif brand_name == 'Redmi' or brand_name == 'Samsung' or brand_name == 'Apple' or brand_name == 'Vivo':
        brand_name = Product.objects.filter(
            category="M").filter(brand=brand_name)
    elif brand_name == 'below':
        brand_name = Product.objects.filter(
            category="M").filter(discount_price__lt=14000)
    elif brand_name == 'above':
        brand_name = Product.objects.filter(
            category="M").filter(discount_price__gte=14000)
    if request.user.is_authenticated:
        return render(request, 'app/mobile.html', {'brand_name': brand_name, 'cart_item_count': Cart.objects.filter(user=request.user).count()})
    else:
        return render(request, 'app/mobile.html', {'brand_name': brand_name, })


def laptop(request, brand_name=None):
    if brand_name == None:
        brand_name = Product.objects.filter(category="L")
    elif brand_name == 'Lenovo' or brand_name == 'Dell' or brand_name == 'Apple' or brand_name == 'HP' or brand_name == 'Asus':
        brand_name = Product.objects.filter(
            category="L").filter(brand=brand_name)
    elif brand_name == 'below':
        brand_name = Product.objects.filter(
            category="L").filter(discount_price__lt=70000)
    elif brand_name == 'above':
        brand_name = Product.objects.filter(
            category="L").filter(discount_price__gte=14000)
    if request.user.is_authenticated:
        return render(request, 'app/laptop.html', {'brand_name': brand_name, 'cart_item_count': Cart.objects.filter(user=request.user).count()})
    else:
        return render(request, 'app/laptop.html', {'brand_name': brand_name, })


def TopWear(request):
    minvalue = request.GET.get('min-value')
    maxvalue = request.GET.get('max-value')
    if minvalue is None:
        product = Product.objects.filter(category="TW")
        if request.user.is_authenticated:
            return render(request, 'app/topwear.html', {'product': product, 'cart_item_count': Cart.objects.filter(user=request.user).count()})
        else:
            return render(request, 'app/topwear.html', {'product': product, })
    else:
        product = Product.objects.filter(category="TW").filter(
            discount_price__gte=minvalue, discount_price__lte=maxvalue)
        if request.user.is_authenticated:
            return render(request, 'app/topwear.html', {'product': product, 'cart_item_count': Cart.objects.filter(user=request.user).count()})
        else:
            return render(request, 'app/topwear.html', {'product': product, })


def BottomWear(request):
    minvalue = request.GET.get('min-value')
    maxvalue = request.GET.get('max-value')
    if minvalue is None:
        product = Product.objects.filter(category="BW")
        if request.user.is_authenticated:
            return render(request, 'app/bottomwear.html', {'product': product, 'cart_item_count': Cart.objects.filter(user=request.user).count()})
        else:
            return render(request, 'app/bottomwear.html', {'product': product, })
    else:
        product = Product.objects.filter(category="BW").filter(
            discount_price__gte=minvalue, discount_price__lte=maxvalue)
        if request.user.is_authenticated:
            return render(request, 'app/bottomwear.html', {'product': product, 'cart_item_count': Cart.objects.filter(user=request.user).count()})
        else:
            return render(request, 'app/bottomwear.html', {'product': product, })


def profile(request):
    if request.method == "POST":
        add = Address()
        add.user = request.user
        add.name = request.POST.get('name')
        add.hno = request.POST.get('hno')
        add.locality = request.POST.get('locality')
        add.street = request.POST.get('street')
        add.city = request.POST.get('city')
        add.state = request.POST.get('state')
        add.pincode = request.POST.get('pincode')
        messages.success(request, "Address added successfully!")
        add.save()
        return render(request, 'app/profile.html', {'states': STATE_CHOICES, 'cart_item_count': Cart.objects.filter(user=request.user).count()})
    else:
        return render(request, 'app/profile.html', {'states': STATE_CHOICES, 'cart_item_count': Cart.objects.filter(user=request.user).count()})


def changepassworddone(request):
    return render(request, 'app/changepassworddone.html', {'cart_item_count': Cart.objects.filter(user=request.user).count()})
# def changepassowrd(request):
#     if request.method == "POST":
#         fm = SetNewPassword(request)
#         return render(request,'app/changepassword.html',{'form':fm})
#     else:
#         fm = SetNewPassword(request)
#         return render(request,'app/changepassword.html',{'form':fm})


"""  We have used inbuilt LoginView for Customer Login Form """
# def login(request):
#     return render(request,'app/login.html')

# class LoginView(View):
#     def get(self,request):
#         fm = CustomerLoginForm()
#         return render(request,'app/login.html',{'fm':fm})
#     def post(self,request):
#         fm = CustomerLoginForm(request.POST)
#         if fm.is_valid():
#             return render(request,'app/login.html',{'fm':fm})
#         return render(request,'app/login.html',{'fm':fm})

"""  
    register view to get registration of new customer CustomerRegistrationForm 
    
    form is used here to create instance of user
"""


def register(request):
    if request.method == "POST":
        fm = CustomerRegistrationForm(request.POST)
        if fm.is_valid():
            fm.save()
            email = request.POST.get('email')
            return redirect(reverse('create_customer', kwargs={'email_': str(email)}))
            # user = User.objects.get(email=request.POST.get('id_email'))
            # new_customer = Customer()
            # new_customer.user = user
            # new_customer.name = user.first_name + user.last_name

            # new_customer.save()
    else:
        fm = CustomerRegistrationForm()
    return render(request, 'app/register.html', {'fm': fm})


def create_customer(request, email_):
    # print(email_)
    user = User.objects.get(email=str(email_))
    new_customer = Customer()
    new_customer.user = user
    new_customer.name = user.first_name + user.last_name
    new_customer.save()
    messages.success(request, "User created successfully!")
    # send_mail(
    # 'Account created successfully!',
    # f'Welcome to shopabble {user.first_name} {user.last_name}!. \n Your account has been created successfully. \n Email: {user.email} \n Happy Shopping! \n Regards Shopabble Developer Team',
    # settings.EMAIL_HOST_USER,
    # [str(user.email)],
    # fail_silently=False,
    # )
    fm = CustomerRegistrationForm()
    return render(request, 'app/register.html', {'fm': fm})


def orders(request):
    if request.user.is_authenticated:
        obj = OrderPlaced.objects.filter(user=request.user)
        orders = []
        for ob in obj:
            orders.append(
                [ob, ob.quantity*Product.objects.get(id=ob.product.id).discount_price])
        return render(request, 'app/orders.html', {'orders': orders})

# def productdetails(request):
#     return render(request,'app/productdetails.html')


class ProductDetailsView(View):
    def get(self, request, pk):
        product = Product.objects.get(id=pk)
        if request.user.is_authenticated:
            is_inside_cart = Cart.objects.filter(
                user=request.user).filter(product=product)
            cart_item_count = Cart.objects.filter(user=request.user).count()
        else:
            is_inside_cart = None
            cart_item_count = None
        return render(request, 'app/productdetails.html', {'product': product, 'is_inside_cart': is_inside_cart, 'cart_item_count': cart_item_count})


def address(request):
    if request.user.is_authenticated:
        addresses = Address.objects.filter(user=request.user)
        return render(request, 'app/address.html', {'addresses': addresses, 'cart_item_count': Cart.objects.filter(user=request.user).count()})
    else:
        return render(request, 'app/address.html')


def cart(request):
    products = Cart.objects.filter(user=request.user)
    shipping_charge = 70.0
    product_amount = sum([prod.product.discount_price *
                         prod.quantity for prod in Cart.objects.filter(user=request.user)])
    total_amount = shipping_charge + product_amount
    return render(request, 'app/cart.html', {'products': products, 'cart_item_count': Cart.objects.filter(user=request.user).count(), 'shipping_charge': shipping_charge, 'product_amount': product_amount, 'total_amount': total_amount})


def add_to_cart(request):
    if request.user.is_authenticated:
        product = Product.objects.get(id=request.GET.get('product_id'))
        Cart(user=request.user, product=product).save()
        shipping_charge = 70.0
        product_amount = sum(
            [prod.product.discount_price*prod.quantity for prod in Cart.objects.filter(user=request.user)])
        total_amount = shipping_charge + product_amount
        return render(request, 'app/cart.html', {'products': Cart.objects.filter(user=request.user), 'messages': ['Item Added Successfully!'], 'cart_item_count': Cart.objects.filter(user=request.user).count(), 'shipping_charge': shipping_charge, 'product_amount': product_amount, 'total_amount': total_amount})
    else:
        return redirect('/acount/login/')


def remove_cart_item(request):
    Cart.objects.get(id=request.GET.get('product_id')).delete()
    shipping_charge = 70.0
    product_amount = sum([prod.product.discount_price *
                         prod.quantity for prod in Cart.objects.filter(user=request.user)])
    total_amount = shipping_charge + product_amount
    return render(request, 'app/cart.html', {'products': Cart.objects.filter(user=request.user), 'messages': ['Item Removed Successfully!'], 'cart_item_count': Cart.objects.filter(user=request.user).count(), 'shipping_charge': shipping_charge, 'product_amount': product_amount, 'total_amount': total_amount})


def alter_quantity(request):
    if request.user.is_authenticated:
        if request.GET.get('action_') == 'increase':
            obj = Cart.objects.get(Q(user=request.user) & Q(
                product=Product.objects.get(id=request.GET.get('product_id'))))
            obj.quantity += 1
            obj.save()
        else:
            obj = Cart.objects.get(Q(user=request.user) & Q(
                product=Product.objects.get(id=request.GET.get('product_id'))))
            if obj.quantity > 1:
                obj.quantity -= 1
            obj.save()
        shipping_charge = 70.0
        product_amount = sum(
            [prod.product.discount_price*prod.quantity for prod in Cart.objects.filter(user=request.user)])
        total_amount = shipping_charge + product_amount
        return render(request, 'app/cart.html', {'products': Cart.objects.filter(user=request.user), 'cart_item_count': Cart.objects.filter(user=request.user).count(), 'shipping_charge': shipping_charge, 'product_amount': product_amount, 'total_amount': total_amount})
    else:
        return redirect('/acount/login/')


def checkout(request):
    if request.user.is_authenticated:
        products = Cart.objects.filter(user=request.user)
        addresses = Address.objects.filter(user=request.user)
        shipping_charge = 70.0
        product_amount = sum(
            [prod.product.discount_price*prod.quantity for prod in Cart.objects.filter(user=request.user)])
        total_amount = shipping_charge + product_amount
        return render(request, 'app/checkout.html', {'products': products, 'addresses': addresses, 'cart_item_count': Cart.objects.filter(user=request.user).count(), 'shipping_charge': shipping_charge, 'product_amount': product_amount, 'total_amount': total_amount})
    else:
        return redirect('/acount/login/')


def paymentdone(request):
    if request.user.is_authenticated:
        products = Cart.objects.filter(user=request.user)
        for product in products:
            placeorder = OrderPlaced()
            placeorder.user = request.user
            placeorder.customer = Customer.objects.get(user=request.user)
            placeorder.product = product.product
            placeorder.quantity = product.quantity
            placeorder.order_date = datetime.now()
            placeorder.save()
            products.delete()
        obj = OrderPlaced.objects.filter(user=request.user)
        orders = []
        for ob in obj:
            orders.append(
                [ob, ob.quantity*Product.objects.get(id=ob.product.id).discount_price])
        return render(request, 'app/orders.html', {'orders': orders})
    else:
        return redirect('/acount/login/')


def resetpassword(request):
    return render(request, 'app/resetpassword.html')


def logout(request):
    return render(request, 'app/login.html')


def buynow(request):
    if request.user.is_authenticated:
        product = Product.objects.get(id=request.GET.get('product_id'))
        Cart(user=request.user, product=product).save()
        return redirect('/checkout/')
    else:
        return redirect('/acount/login/')
