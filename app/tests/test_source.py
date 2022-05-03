import unittest
from app.models import Source


class SourceTest(unittest.TestCase):

    def setUp(self):
        self.new_source = Source('engadget','Engadget')

    def test_instance(self):
        self.assertTrue(isinstance( self.new_source,Source))

