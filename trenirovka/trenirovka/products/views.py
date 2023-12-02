from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import DetailView
from products.models import Product, ProductCategory, Basket
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from common.views import TitleMixin


class IndexView(TitleMixin, TemplateView):
    template_name = 'products/index.html'
    title = 'Store'

class SuccessView(TitleMixin, TemplateView):
    template_name = 'products/success.html'
    title = 'Store - Оформить заказ'

class OrdersView(TitleMixin, TemplateView):
    template_name = 'products/orders.html'
    title = 'Store - Заказы'

class OrderView(TitleMixin, TemplateView):
    template_name = 'products/order.html'
    title = 'Store - Заказ'


class CreateOrderView(TitleMixin, TemplateView):
    template_name = 'products/order-create.html'
    title = 'Store - Оформить заказ'


class ProductsListView(TitleMixin, ListView):
    model = Product
    template_name = 'products/products.html'
    paginate_by = 3
    title = 'Store - Каталог'


    def get_queryset(self):
        queryset = super(ProductsListView, self).get_queryset()
        category_id = self.kwargs.get('category_id')
        return queryset.filter(category__id=category_id) if category_id else queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductsListView, self).get_context_data()
        context['categories'] = ProductCategory.objects.all()
        return context

    def get_absolute_url(self):
        return reverse("products:product_detail", kwargs={"pk": self.pk})


class ProductDetailView(DetailView):
    template_name = 'products/product_detail.html'
    model = Product
    queryset = Product.objects.all()
    slug_field = "pk"

@login_required
def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product = product)
    if not baskets.exists():
        Basket.objects.create(user=request.user, product= product, quantity=1)
    else:
        basket = baskets.first()
        basket.quantity+=1
        basket.save()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
@login_required
def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])




