#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.test import TestCase


class ToolboxTest(TestCase):
    
    def test_unicodecsv(self):
        """
        Test simple usage of the unicodecsv toy.
        """
        import csv
        from toolbox import unicodecsv
        from cStringIO import StringIO
        d = StringIO.StringIO()
        d.write("Name,Type,County\n")
        d.write("La Cañada Flintridge,Neighborhood,L.A.County\n")
        d.write("Downtown,Neighborhood,L.A.County\n")
        reader = unicodecsv.UnicodeDictReader(d)
        for row in reader: print row
        print list(reader)
#        print list(reader)
#        reader.next()
#        reader.__iter__()
#        self.assertEqual(type(list(reader)), type([]))
