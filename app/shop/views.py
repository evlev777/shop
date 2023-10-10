from django.shortcuts import render
from django.views.generic import ListView

from .models import Product, Categorry, Brand, Size, Specification, Gender


class ProductListView(ListView):
    model = Product
    # queryset = model.objects.all()
    template_name = 'shop/index.html'

    # def get_queryset(self):
    #     queryset = self.queryset
    #     if self.kwargs.get("category_id"):
    #         queryset = queryset.filter(category__slug=self.kwargs.get("category_id"))
    #     return queryset