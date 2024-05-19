"""
URL configuration for Ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ecommerceapp import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('index', views.index),
    path('about', views.about),
    path('contact', views.contact),
    path('products', views.products),
    path('singleproduct/<int:prod_id>', views.singleproduct),
    path('login', views.signin),
    path('signup',views.signup),
    path('logout', views.signout),
    path('changeps',views.change_password),
    path('password_reset/', views.password_reset_request, name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('user', views.Userprofile),
    path('adminlogin', views.adminlogin),
    path('dashboard', views.dashboard),
    path('adminadproduct', views.submitproduct),
    path('submit',views.submitproduct),
    path('adminread', views.adminread),
    path('adminupdate/<int:id>',views.adminupdate),
    path('delete/<int:id>',views.delete),
    path('bag/<int:prod_id>/<str:user>',views.bag),
    path('admin_signout',views.admin_signout),
    path('cart',views.mycart),
    path('checkout',views.checkout),
    path('deletepro/<int:id>',views.deletepro),
    path('status/<int:id>',views.status),
    path('manageorder',views.manageorder),
    path('redirect_url/', views.redirect_view, name='redirect_view'),
]


if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)