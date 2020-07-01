from django.test import TestCase


class URLTests(TestCase):
    def test_postpage(self):
        response = self.client.get('posts/')
        self.assertEquals(response.status_code, 404)
