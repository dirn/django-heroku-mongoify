#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

import os

from mongoify import mongoify


class MongoifyTest(unittest.TestCase):
    def setUp(self):
        os.environ.pop('MONGO_URI', None)
        os.environ.pop('OTHER_MONGO_URI', None)
        os.environ.pop('ANOTHER_MONGO_URL', None)

    def test_all(self):
        """Test all settings"""

        os.environ['MONGO_URI'] = 'mongodb://localhost/environ'
        os.environ['OTHER_MONGO_URI'] = 'mongodb://localhost/other'

        uris = mongoify(default='mongodb://localhost/default')

        self.assertEqual(uris['default'], 'mongodb://localhost/environ')
        self.assertEqual(uris['OTHER_MONGO'], 'mongodb://localhost/other')

    def test_default(self):
        """Test passing a default value"""

        uris = mongoify(default='mongodb://localhost/default')

        self.assertEqual(uris['default'], 'mongodb://localhost/default')

    def test_mongo_uri(self):
        """Test `MONGO_URI` setting"""

        os.environ['MONGO_URI'] = 'mongodb://localhost/environ'

        uris = mongoify(default='mongodb://localhost/default')

        self.assertEqual(uris['default'], 'mongodb://localhost/environ')

    def test_none(self):
        """Test no values at all"""

        uris = mongoify()

        self.assertEqual(uris, {})

    def test_others(self):
        """Test other environment settings"""

        os.environ['OTHER_MONGO_URI'] = 'mongodb://localhost/other'
        os.environ['ANOTHER_MONGO_URL'] = 'mongodb://localhost/another'

        uris = mongoify()

        self.assertTrue('default' in uris)
        self.assertEqual(uris['OTHER_MONGO'], 'mongodb://localhost/other')
        self.assertEqual(uris['ANOTHER_MONGO'], 'mongodb://localhost/another')
