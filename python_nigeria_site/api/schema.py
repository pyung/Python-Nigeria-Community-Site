from graphene import ObjectType, Node, Schema
from graphene_django.types import DjangoObjectType
from graphene_django.fields import DjangoConnectionField

from python_nigeria_site.store.models import Product


class ProductNode(DjangoObjectType):
    class Meta:
        model = Product
        filter_fields = ['product_name', 'product_code', 'group', 'created_on']


class Query(ObjectType):
    product = graphene.List(ProductNode)

    def resolve_all_products(self, info, **kwargs):
        return Product.objects.all()

    def resolve_product(self, info, **kwargs):
        product_id = kwargs.get('id')
        if not product_id: 
            return None
        return Product.objects.get(pk=product_id)


schema = Schema(query=Query)