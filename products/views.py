from django.views.generic import TemplateView
from django.views.generic.list import ListView

from products.models import Product, ProductCategory

# Create your views here.


class IndexView(TemplateView):
    template_name = 'products/index.html'
    title = 'Store'


class ProductsListView(ListView):
    model = Product
    template_name = 'products/products.html'
    context_object_name = 'products'
    paginate_by = 3
    title = 'Store - Каталог'

    def get_queryset(self):
        queryset = Product.objects.all()
        category_id = self.kwargs.get('category_id')
        return queryset.filter(category_id=category_id) if category_id else queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductsListView, self).get_context_data()
        context['categories'] = ProductCategory.objects.all()
        return context
