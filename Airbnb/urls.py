from django.contrib import admin
from django.urls import path,include 
from accounts import views as accounts_views 

urlpatterns = [
    path('admin/', admin.site.urls),
]
