from django.urls import path
from . import views

urlpatterns = [

    path('',views.home,name='home'),
    path('product/<int:id>/',views.product,name='product'),
    path('about/',views.about,name='about'),
    path('category/<str:foods>/',views.category,name='category'),
    path('login/',views.login_user,name='login'),
    path('logout/',views.logout_user,name='logout'),
    path('register/',views.register_user,name='register'),
    


]
