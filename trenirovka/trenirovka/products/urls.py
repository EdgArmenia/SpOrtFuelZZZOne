
from django.urls import path
from products.views import *
app_name = 'products'

urlpatterns = [

    path('', ProductsListView.as_view(), name="index"),
    path('category/<int:category_id>/', ProductsListView.as_view(), name="category"),
    path('page/<int:page>/', ProductsListView.as_view(), name="paginator"),
    path('baskets/add/<int:product_id>/', basket_add, name='basket_add'),
    path('baskets/remove/<int:basket_id>/', basket_remove, name='basket_remove'),
    path('orders/order/', OrderView.as_view(), name='order'),
    path('baskets/create_order/', CreateOrderView.as_view(), name='create_order'),
    path('baskets/create_order/success/', SuccessView.as_view(), name='success'),
    path('orders/', OrdersView.as_view(), name='orders'),

]
