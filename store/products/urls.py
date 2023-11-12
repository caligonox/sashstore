from django.urls import path

from products.views import ProductsListView, basket_add, basket_remove

app_name = 'products'

urlpatterns = [
    path('', ProductsListView.as_view(), name='index'),
    path('<int:category_id>/', ProductsListView.as_view(), name='category'),
    path('page/<int:page>/', ProductsListView.as_view(), name='paginator'),
    path('basket_add/<int:product_id>/', basket_add, name='basket_add'),
    path('basket_remove/<int:id>/', basket_remove, name='basket_remove'), 
]