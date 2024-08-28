from django.db import models
import datetime
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name="نام دسته بندی")
    slug = models.SlugField(
        max_length=300, unique=True, allow_unicode=True, verbose_name="آدرس دسته بندی"
    )

    class Meta:
        ordering = ("name",)
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("category_detail", kwargs={"slug": self.slug})


class Product(models.Model):
    name = models.CharField(max_length=30, verbose_name="نام محصول")
    description = models.TextField(verbose_name="توضیحات")
    price = models.IntegerField(verbose_name="قیمت")
    image = models.ImageField(upload_to="image/products/", verbose_name="تصویر")
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, default=1, verbose_name="دسته بندی"
    )

    class Meta:
        ordering = ("name",)
        verbose_name = "محصول"
        verbose_name_plural = "محصولات"

    def __str__(self):
        return self.name


class Customer(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="نام")
    last_name = models.CharField(max_length=50, verbose_name="نام خانوادگی")
    email = models.EmailField(verbose_name="ایمیل")
    phone = models.CharField(max_length=20, verbose_name="شماره تلفن")
    address = models.CharField(max_length=100, verbose_name="آدرس")
    zipcode = models.CharField(max_length=10, verbose_name="کد پستی")
    city = models.CharField(max_length=20, verbose_name="شهر")
    country = models.CharField(max_length=20, verbose_name="کشور")
    password = models.CharField(max_length=20, verbose_name="رمز عبور")

    class Meta:
        verbose_name = "مشتری"
        verbose_name_plural = "مشتریان"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="محصول")
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, verbose_name="مشتری"
    )
    quantity = models.IntegerField(default=1, verbose_name="تعداد")
    address = models.CharField(
        max_length=200, default="", blank=True, verbose_name="آدرس"
    )
    phone = models.CharField(
        max_length=20, default="", blank=True, verbose_name="شماره تلفن"
    )
    date = models.DateField(default=datetime.date.today, verbose_name="تاریخ")
    status = models.BooleanField(default=False, verbose_name="وضعیت")

    class Meta:
        ordering = ("-date",)  # ترتیب بر اساس تاریخ
        verbose_name = "سفارش"
        verbose_name_plural = "سفارشات"

    def __str__(self):
        return f"سفارش {self.product.name} برای {self.customer.first_name} {self.customer.last_name}"
