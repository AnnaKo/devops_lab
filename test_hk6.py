#!/usr/bin/python

import unittest
import hk6

class Testhk6(unittest.TestCase):

    def setUp(self):
        """Init"""

    def test_hk6_json(self):
        """Test for main"""
        self.assertTrue(hk6.ako_json())
        
    def test_hk6_yaml(self):
        """Test for main"""
        self.assertTrue(hk6.ako_yaml())

    def tearDown(self):
        """Finish"""