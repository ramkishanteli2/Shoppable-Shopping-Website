from django.contrib import admin
from django.urls import path, include
from app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import CustomerLoginForm, SetNewPassword, ResetPasswordForm, SetNewPasswordForm
urlpatterns = [
    path('', views.ProductView.as_view(), name="home"),
    # path('',views.index,name="home"),
    path('mobile/', views.mobile, name="mobile"),
    path('mobile/<slug:brand_name>', views.mobile, name="mobile"),
    path('laptop/', views.laptop, name="laptop"),
    path('laptop/<slug:brand_name>', views.laptop, name="laptop"),
    path('acount/login/', auth_views.LoginView.as_view(template_name='app/login.html',
         authentication_form=CustomerLoginForm), name="login"),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name="logout"),
    path('register/', views.register, name="register"),
    path('create_customer/<str:email_>',
         views.create_customer, name="create_customer"),
    path('cart/', views.cart, name='cart'),
    path('chekcout/', views.checkout, name='checkout'),
    path('paymentdone/', views.paymentdone, name='paymentdone'),
    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path('remove_cart_item/', views.remove_cart_item, name='remove_cart_item'),
    path('alter_quantity', views.alter_quantity, name='alter_quantity'),
    path('buynow/', views.buynow, name='buynow'),
    path('profile/', views.profile, name='profile'),
    path('orders/', views.orders, name='orders'),
    # path('changepassword/',auth_views.SetNewPassword.as_view(template_name='app/changepassword',authentication_form=)),
    path('changepassword/', auth_views.PasswordChangeView.as_view(template_name='app/changepassword.html',
         form_class=SetNewPassword, success_url='/changepassworddone/'), name='changepassword'),
    path('changepassworddone/', views.changepassworddone,
         name='changepassworddone'),
    path('address/', views.address, name='address'),
    path('productdetails/<int:pk>',
         views.ProductDetailsView.as_view(), name='productdetails'),
    path('checkout/', views.checkout, name='check-out'),
    path('resetpassword/', auth_views.PasswordResetView.as_view(template_name='app/resetpassword.html',
         form_class=ResetPasswordForm), name='password_reset'),
    path('resetpassword/done', auth_views.PasswordResetDoneView.as_view(
        template_name='app/passwordresetdone.html'), name='password_reset_done'),
    path('resetpasswordconfirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='app/passwordresetconfirm.html', form_class=SetNewPasswordForm), name='password_reset_confirm'),
    path('resetpasswordcomplete', auth_views.PasswordResetCompleteView.as_view(
        template_name='app/passwordresetcomplete.html'), name='password_reset_complete'),
    # path('resetpassword/',views.resetpassword,name='reset-password'),
    path('topwear/', views.TopWear, name="topwear"),
    path('bottomwear/', views.BottomWear, name="bottomwear"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
