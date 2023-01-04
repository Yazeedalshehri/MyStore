"""MyStore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from base import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('UserLogin/',views.UserLogin),
    path('Cart/',views.Cart),
    path('admin/', admin.site.urls),
    path('HomePage/',views.HomePage, name="homepage"),
    path('HomePage/Register/',views.Register),
    path('HomePage/Login/',views.Login),
    path('<slug:slug>/',views.AdminPage , name = "AdminPage"),
    path('<slug:slug>/Analytics/',views.Analytics),
    path('<slug:slug>/Customers/',views.Customers),
    path('<slug:slug>/Products/',views.Products),
    path('<slug:slug>/Orders/',views.Orders),
    path('<slug:slug>/Settings/',views.Settings),
    path('<slug:slug>/store/',views.Store),
   
    

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
