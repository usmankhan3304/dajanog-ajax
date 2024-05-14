
from django.contrib import admin
from django.urls import path
from app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="home"),
    path('submit-data/',views.officeCrud,name="home"),
    path('empsuccess/',views.empCrud,name="emp"),
    path('offices/',views.getoffices,name="offices")
]
