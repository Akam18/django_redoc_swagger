from django.db import models
from autoslug import AutoSlugField
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название категории")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создано")

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

def slugify_fun(content):
    return slugify(content)        

class Product(models.Model):
    slug = AutoSlugField(populate_from=slugify_fun, unique=True, editable=False)

    # 2
    # slug = AutoSlugField(populate_from='name')

    # 1
    # slug = models.SlugField(max_length= 100, unique=True, verbose_name="URL slug")
    image = models.ImageField(upload_to="product/", verbose_name="Picture")        
    name = models.CharField(max_length=100, verbose_name="Product Name")
    price = models.PositiveIntegerField(verbose_name="Product Price")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Дата создания")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создано")

    def __str__(self) -> str:
        return f"{self.name} - {self.price} - {self.created_at}"
    
    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["-created_at"]
