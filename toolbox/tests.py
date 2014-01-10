#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.test import TestCase


class ToolboxTest(TestCase):
    
    TEST_CSV = """Name,Type,County
La Cañada Flintridge,Neighborhood,L.A.County
Downtown,Neighborhood,L.A.County
"""

    def test_unicodecsv(self):
        """
        Test simple usage of the unicodecsv toy.
        """
        import csv
        from toolbox import unicodecsv
        from cStringIO import StringIO
        d = StringIO(self.TEST_CSV)
        reader = unicodecsv.UnicodeDictReader(d)
        reader.next()
        reader.__iter__()
        self.assertEqual(type(list(reader)), type([]))
