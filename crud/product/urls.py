from django.contrib import admin
from django.urls import path
from .views import *

from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   path('home/',view_index, name="home"),
   path('product/',view_add_product),
   path('product/save',view_productdata_save),
   path('product/productlist',view_product_lists, name="productlist"),
   path('product/edit/<int:ID>',view_productdata_updateform),
   path('product/edit/update/<int:ID>',view_update_form_data_in_db),
   path('product/delete/<int:ID>', view_delete), 
   # path('user/register', view_login_page),
   path('signup/',view_register_user, name="signup"),
   path('restrictpage/',view_authenticate_user, name="login"),
   path("welcome/", view_logout_request, name="logout"),
   path("our-product/", view_our_product, name="ourproduct"),
   path('search/',view_search, name="search"),
]