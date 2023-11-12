from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse

from products.models import Product, ProductCategory


class IndexViewTestCase(TestCase):
    fixtures = ['categorys.json', 'goods.json']
    
    def test_view(self):
        path = reverse('index')
        response = self.client.get(path)

class ProductsListViewTestCase(TestCase):

    def _common_tests(self, response):
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data['title'], 'Store')
        self.assertTemplateUsed(response, 'products/products.html')
        
    def test_list(self):
        path = reverse('products:index')
        response = self.client.get(path)

        products = Product.objects.all()

        self._common_tests(response)


    def test_list_with_category(self):
        category = ProductCategory.objects.first()
        path = reverse('products:category', kwargs={'category_id': category.id})
        response = self.client.get(path)




