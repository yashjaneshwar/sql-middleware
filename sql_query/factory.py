import factory
from factory.faker import faker

from .models import Product

FAKE = faker.Faker()

class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product
    
    name = factory.Faker('sentence', nb_words=12)
    slug = factory.Faker('slug')
    is_digital = False


""" 
IN SHELL

    # CREATE DUMMY DATA OF SIZE 100
    >>> from sql_query.factory import ProductFactory
    >>> x = ProductFactory.create_batch(100)

    # INPECTING DUMMY DATA
    >>> from sql_query.models import Product
    >>> x = Product.objects.all()

    >>> x
    <QuerySet [<Product: Offer smile foot strategy ready thank listen seem woman word.>, <Product: Media actually perhaps choice real task eight.>, '...(remaining elements truncated)...']>

    >>> x.count()
    100
    >>> exit()

"""