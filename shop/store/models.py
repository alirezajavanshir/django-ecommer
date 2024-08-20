from django.db import models
import datetime



class Category(models.Model):
     name=models.CharField(max_length=20,verbose_name='نام')


     def __str__(self):
        return self.name



class Product(models.Model):
    name=models.CharField(max_length=30 ,verbose_name= 'نام')
    description=models.TextField(verbose_name= 'توضیحات')
    price=models.IntegerField(verbose_name= 'قیمت')
    image=models.ImageField(upload_to='image/products/', verbose_name= 'تصویر')
    category=models.ForeignKey(Category,on_delete=models.CASCADE,default=1,verbose_name='دسته بندی')   

    def __str__(self):
        return self.name


class Customer(models.Model):

    first_name=models.CharField(max_length=50,verbose_name='نام')
    last_name=models.CharField(max_length=50,verbose_name='نام خانوادگی')
    email=models.EmailField(verbose_name='ایمیل')
    phone=models.CharField(max_length=20, verbose_name='شماره تلفن')
    address=models.CharField(max_length=100,verbose_name='آدرس')
    zipcode=models.CharField(max_length=10,verbose_name='کد پستی')
    city=models.CharField(max_length=20,verbose_name='شهر')
    country=models.CharField(max_length=20,verbose_name='کشور')
    password=models.CharField(max_length=20,verbose_name='رمز عبور')

    def __str__(self):
       return f'{self.first_name} {self.last_name}'


    



class Order(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE,verbose_name='محصول')
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE,verbose_name='مشتری')
    quantity=models.IntegerField(default=1,verbose_name='تعداد')
    address=models.CharField(max_length=200,default='',blank=True,verbose_name='آدرس')
    phone=models.CharField(max_length=20,default='',blank=True,verbose_name='شماره تلفن')
    date=models.DateField(default=datetime.datetime.today,verbose_name='تاریخ')
    status=models.BooleanField(default=False,verbose_name='وضعیت')


    def __str__(self):
       return self.product
    

