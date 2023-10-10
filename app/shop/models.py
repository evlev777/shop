from django.db import models
from django.db.models import Q
from django.db.models.functions import Length

models.CharField.register_class_lookup(Length)

class Categorry(models.Model):
    name = models.CharField(
        max_length=32,
        null=False,
        blank=False,
        unique=True,
        verbose_name="название"
    )

    slug = models.SlugField(
        max_length=32,
        null=False,
        blank=False,
        unique=True,
        verbose_name="URL"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ('name', )
        constraints = (
            models.CheckConstraint(check=Q(name__length__gte=2), name='category_name_length'),
            models.CheckConstraint(check=Q(slug__length__gte=2), name='category_slug_length')
        )

class Size(models.Model):
    name = models.CharField(
        max_length=4,
        null=False,
        blank=False,
        unique=True,
        verbose_name='размер'
    )

    slug = models.SlugField(
        max_length=4,
        blank=False,
        null=False,
        unique=True,
        verbose_name='URL'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'размер'
        verbose_name_plural = 'размеры'
        ordering = ('name', )
        constraints = (
            models.CheckConstraint(check=Q(name__length__gte=1), name='size_name_length'),
            models.CheckConstraint(check=Q(slug__length__gte=1), name='size_slug_length')
        )


class Gender(models.Model):
    name = models.CharField(
        max_length=5,
        blank=False,
        null=False,
        unique=True,
        verbose_name='гендер'
    )

    slug = models.SlugField(
        max_length=5,
        blank=False,
        null=False,
        unique=True,
        verbose_name='URL'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'гендер'
        verbose_name_plural = 'гендера'
        ordering = ('name', )
        constraints = (
            models.CheckConstraint(check=Q(name__length__gte=3), name="gender_name_length"),
            models.CheckConstraint(check=Q(slug__length__gte=3), name="gender_slug_length")
        )

class Brand(models.Model):
    name = models.CharField(
        max_length=64,
        blank=False,
        null=False,
        unique=True,
        verbose_name='бренд'
    )

    slug = models.SlugField(
        max_length=64,
        blank=False,
        null=False,
        unique=True,
        verbose_name='URL'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'бренд'
        verbose_name_plural = 'бренды'
        ordering = ('name', )
        constraints = (
            models.CheckConstraint(check=Q(name__length__gte=2), name='brand_name_length'),
            models.CheckConstraint(check=Q(slug__length__gte=2), name='brand_slug_length')
        )

class Specification(models.Model):
    name = models.CharField(
        max_length=32,
        blank=False,
        null=False,
        unique=True,
        verbose_name='спецификация'
    )

    slug = models.SlugField(
        max_length=32,
        blank=False,
        null=False,
        unique=True,
        verbose_name='URL'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'спецификация'
        verbose_name_plural = 'спецификации'
        ordering = ('name', )
        constraints = (
            models.CheckConstraint(check=Q(name__length__gte=2), name="specification_name_length"),
            models.CheckConstraint(check=Q(slug__length__gte=2), name="specification_slug_length")
        )


class Product(models.Model):
    title = models.CharField(
        max_length=128,
        blank=False,
        null=False,
        unique=True,
        verbose_name='название продукта'
    )

    slug = models.SlugField(
        max_length=128,
        blank=False,
        null=False,
        unique=True,
        verbose_name='URL'
    )

    price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        null=False,
        blank=False,
        verbose_name='цена'
    )
    image = models.ImageField(verbose_name='картинка')
    brand = models.ForeignKey(to='Brand', on_delete=models.CASCADE, verbose_name='бренд')
    description = models.TextField(verbose_name='описание')
    color = models.TextField(verbose_name='цвет', help_text='Вводите цвета через пробел')
    specification = models.ManyToManyField(to='Specification', verbose_name='спецификация')
    size = models.ManyToManyField(to='Size', verbose_name='размер')


    def specification_display(self):
        return ', '.join([specification.name for specification in self.specification.all()])

    def size_display(self):
        return ', '.join([size.name for size in self.size.all()])

    specification_display.short_description = 'Specification'
    size_display.short_description = 'Size'

    @property
    def get_color(self):
        return "/".join(list(self.color))

    @property
    def get_price(self):
        return f'${self.price}'

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
        ordering = ('title', 'price', 'brand', )
        constraints = (
            models.CheckConstraint(check=Q(title__length__gte=2), name='product_name_length'),
            models.CheckConstraint(check=Q(slug__length__gte=2), name='product_slug_length'),
            models.CheckConstraint(check=Q(price__gt=0), name='product_price_length')
        )
