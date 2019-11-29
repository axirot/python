from django.db import models
class ProductCategory(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    name = models.CharField(verbose_name='imya categorii', max_length=64, unique=True)
    desc = models.TextField(verbose_name='opisanie categorii', blank=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='imya producta', max_length=128)
    image = models.ImageField(upload_to='products_images', blank=True)
    short_desc = models.CharField(verbose_name='kratko', max_length=60, blank=True)
    description = models.TextField(verbose_name='podrobno', blank=True)
    price = models.DecimalField(verbose_name='cena', max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(verbose_name='sklad', default=0)
    is_hot = models.BooleanField(verbose_name='goryachi product', default=False)

    def __str__(self):
        return "{} ({})".format(self.name, self.category.name)