from django.views.generic import DetailView, RedirectView
from django.shortcuts import get_object_or_404, render, redirect
from .models import Product, Category
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic.edit import CreateView
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import SignUpForm
from django.urls import reverse_lazy


def navbar_context(request):
    categories = Category.objects.all()
    return {
        "categories": categories,
    }


def home(request):
    products = Product.objects.all()
    return render(request, "home.html", {"products": products})


class CategoryDetailView(DetailView):
    model = Category
    template_name = "category.html"
    context_object_name = "category"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = self.get_object()  # دریافت شیء فعلی (دسته‌بندی)
        products = Product.objects.filter(
            category=category
        )  # فیلتر کردن محصولات بر اساس دسته‌بندی
        context["products"] = products  # اضافه کردن محصولات به context
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = "product.html"
    context_object_name = "product"


class CustomLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = "login.html"

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "شما با موفقیت وارد شدید.")
        return response

    def form_invalid(self, form):
        messages.error(self.request, "نام کاربری یا رمز عبور اشتباه است.")
        return super().form_invalid(form)


class RegisterUserView(CreateView):
    form_class = SignUpForm
    template_name = "register.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        response = super().form_valid(form)
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password1"]
        user = authenticate(username=username, password=password)
        if user is not None:
            login(self.request, user)
            messages.success(self.request, "ثبت نام با موفقیت انجام شد.")
        return response

    def form_invalid(self, form):
        messages.error(
            self.request, "ثبت نام ناموفق بود. لطفاً فیلدها را به درستی پر کنید."
        )
        return super().form_invalid(form)


class LogoutView(RedirectView):
    url = reverse_lazy("home")

    def get(self, request, *args, **kwargs):
        logout(request)
        messages.success(request, "با موفقیت از حساب کاربری خود خارج شدید.")
        return super().get(request, *args, **kwargs)


def about(request):
    return render(request, "about.html", {})
