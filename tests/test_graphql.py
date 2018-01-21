import django.test import TestCase
from django.test import Client

from python_nigeria_site.store.models import Product

class TestGraphQL(TestCase):
    def setUp(self):
        self._client = Client()
        self.product_details = {"product_name": "A", "unit_price":3000, "description": "It is a product", "product_code": "abcdef"}

    def query(self, query, operation=None, input_=None):
         '''
        Args:
            query (string) - GraphQL query to run
            operation (string) - If the query is a mutation or named query, you must
                               supply the operation.  For annon queries ("{ ... }"),
                               should be None (default).
            inpu_t (dict) - If provided, the $input variable in GraphQL will be set
                           to this value

        Returns:
            dict, response from graphql endpoint.  The response has the "data" key.
                  It will have the "error" key if any error happened.
        '''
        body = {'query': query}
        if operation:
            body['operation_name'] = operation
        if input_:
            body['variables'] = {'input': input_}

        resp = self._client.post('/graphql', json.dumps(body),
                                 content_type='application/json')
        resp = json.loads(resp.content.decode())
        return resp

    def assertResponseNoErrors(self, resp: dict, expected: dict):
        '''
        Assert that the resp (as retuened from query) has the data from
        expected
        '''
        self.assertNotIn('errors', resp, 'Response had errors')
        self.assertEqual(resp['data'], expected, 'Response has correct data')

    def test_create_product_mutation(self):
        product = Product.objects.create(self.product_details)
        query = '''
                query ProductQuery {
                        product {
                            product_name,
                        }
                    }
                '''
    
    def test_update_product_mutation(self):
        pass
    
    def test_delete_product_mutation(self):
        pass


