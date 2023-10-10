from django.contrib import admin
from .models import Product, Categorry, Size, Specification, Brand, Gender

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', )
    prepopulated_fields = {
        'slug': ('name', )
    }

@admin.register(Categorry)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )
    prepopulated_fields = {
        'slug': ('name',)
    }

@admin.register(Gender)
class GenderAdmin(admin.ModelAdmin):
    list_display = ('name', )
    prepopulated_fields = {
        'slug': ('name',)
    }

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title',
                    'price',
                    'description',
                    'size_display',
                    'specification_display',
                    'brand',
                    'color',
                    'image',
                    )

    list_filter = ('title',
                   'price',
                   'brand',
                   )

    prepopulated_fields = {
        'slug': ('title',)
    }

@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = ('name', )
    prepopulated_fields = {
        'slug': ('name',)
    }

@admin.register(Specification)
class SpecificationAdmin(admin.ModelAdmin):
    list_display = ('name', )
    prepopulated_fields = {
        'slug': ('name',)
    }






