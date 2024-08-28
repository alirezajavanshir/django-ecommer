from django.urls import re_path, path
from . import views
from .views import (
    CategoryDetailView,
    ProductDetailView,
    CustomLoginView,
    RegisterUserView,
    LogoutView,
)

urlpatterns = [
    re_path(
        r"^category/(?P<slug>[-\w]+)/$",
        CategoryDetailView.as_view(),
        name="category_detail",
    ),
    path("product/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("register/", RegisterUserView.as_view(), name="register"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("about/", views.about, name="about"),
    path("", views.home, name="home"),
]
