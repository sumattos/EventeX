"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase


<<<<<<< HEAD
#class SimpleTest(TestCase):
#    def test_basic_addition(self):
#        """
#        Tests that 1 + 1 always equals 2.
#        """
#        self.assertEqual(1 + 1, 2)


class HomepageUrlTest(TestCase):
	def test_success_when_get_homepage(self):
	    response = self.client.get('/')
	    self.assertEquals(200, response.status_code)
	    self.assertTemplateUsed(response, 'index.html')
=======
class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)
>>>>>>> 7e9a5f74fac19b7df090d300bcc22f8c3578a934
