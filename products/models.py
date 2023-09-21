from django.db import models

# Create your models here.


class ProductCategory(models.Model):
    '''Категория товара'''
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self) -> str:
        return self.name


class CarBrand(models.Model):
    '''Марка автомобиля'''
    name = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to='images/car_brands_images', blank=True, null=True)

    class Meta:
        verbose_name = "Марка автомобиля"
        verbose_name_plural = "Марки автомобилей"

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    '''Товар'''
    name = models.CharField(max_length=256)
    description = models.TextField()
    article = models.CharField(max_length=6, unique=True)
    image = models.ImageField(upload_to='images/products_images')
    category = models.ForeignKey('ProductCategory', on_delete=models.CASCADE)
    car_brand = models.ForeignKey('CarBrand', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    in_stock = models.BooleanField()

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self) -> str:
        return self.name
