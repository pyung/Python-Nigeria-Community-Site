from test_plus.test import TestCase
from python_nigeria_site.store.models import Product
from python_nigeria_site.users.models import User


class TestUser(TestCase):

    def setUp(self):
        # self.user = self.make_user() ##
        user_details = {"name": "Olamilekan Wahab", "email":"olamyy53@gmail.com"}
        self.user = User(user_details)

    def test__str__(self):
        self.assertEqual(
            self.user.__str__(),
            'testuser'  # This is the default username for self.make_user()
        )

    def test_get_absolute_url(self):
        self.assertEqual(
            self.user.get_absolute_url(),
            '/users/testuser/'
        )
    
    def test_create_user(self):
        user = self.user.save()
        self.assertIsInstance(User, User.objects.get(name="Olamilekan Wahab"))
    
    def tearDown(self):
        self.user.delete()


class TestStore(TestCase):
    def setUp(self):
        product_details = {"product_name": "A", "unit_price":3000, "description": "It is a product", "product_code": "abcdef"}
        self.product = Product(product_details)

    def tearDown(self):
        self.store.delete()

    def test_create_user(self):
        product = self.product.save()
        self.assertIsInstance(Product, Product.objects.get(product_name="A"))

    def test_update_product(self):
        product = self.product.save()
        product = Product.objects.get(product_name="A")
        product.unit_price = 50000
        product.save()
        self.assertEqual(product.unit_price, 50000)

    def test_get_product(self):
        product = self.product.save()
        product = Product.objects.get(product_name="A")
        self.assertIsInstance(Product, Product.objects.get(product_name="A"))



