from django.test import TestCase
from django.urls import resolve

from .. import views

class SolosURLsTestCase(TestCase):
    """
    Test that the root of the site resolves to the
    correct view function
    """
    root = resolve('/')
    self.assertEqual(root.func,views.index)
