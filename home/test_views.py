from django.test import TestCase
from django.urls import reverse


class TestHomeView(TestCase):

    def test_home_view_response(self):
        '''
        Test that the home view returns a code 200 and uses the
        correct template.
        '''
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')