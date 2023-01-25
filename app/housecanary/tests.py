from django.test import TestCase
import json

# Create your tests here.
class TestCalls(TestCase):
    def test_get_have_septic(self):
        response = json.loads(self.client.get('/property/septic').content)
        self.assertEqual(response["validated"], True)
