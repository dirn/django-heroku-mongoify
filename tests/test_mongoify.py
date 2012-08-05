#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

import os
import sys

from mongoify import mongoify

sys.path.insert(0, os.path.abspath('..'))
sys.path.append('.')


class MongoifyTest(unittest.TestCase):
    def setUp(self):
        # URL for localhost
        self.localhost = 'mongodb://localhost'
        # URL for MongoHQ
        self.mongohq = \
            'mongodb://mongohq:password@example.mongohq.com:27017/test'
        # URL for MongoLab
        self.mongolab = \
            'mongodb://mongolab:password@example.mongolab.com:27017/test'

        # If the provider URLs already exist in the environment,
        # back them up and delete them.
        if 'MONGOHQ_URL' in os.environ:
            self.MONGOHQ_URL = os.environ['MONGOHQ_URL']
            del os.environ['MONGOHQ_URL']
        else:
            self.MONGOHQ_URL = None
        if 'MONGOLAB_URI' in os.environ:
            self.MONGOLAB_URI = os.environ['MONGOLAB_URI']
            del os.environ['MONGOLAB_URI']
        else:
            self.MONGOLAB_URI = None

    def tearDown(self):
        # Restore any provider URLs to the environment or remove any
        # temporary ones left over from testing.
        if self.MONGOHQ_URL is not None:
            os.environ['MONGOHQ_URL'] = self.MONGOHQ_URL
        elif 'MONGOHQ_URL' in os.environ:
            del os.environ['MONGOHQ_URL']
        if self.MONGOLAB_URI is not None:
            os.environ['MONGOLAB_URI'] = self.MONGOLAB_URI
        elif 'MONGOLAB_URI' in os.environ:
            del os.environ['MONGOLAB_URI']

    def test_default(self):
        """Test passing a default value"""
        connection = mongoify(default=self.localhost)

        self.assertEqual(connection, self.localhost)

    def test_no_default(self):
        """Test passing no default value"""
        connection = mongoify()

        self.assertTrue(connection is None)

    def test_mongohq(self):
        """Test using MONGOHQ_URL"""
        os.environ['MONGOHQ_URL'] = self.mongohq

        connection = mongoify()

        self.assertEqual(connection, self.mongohq)

    def test_mongohq_trumps_all(self):
        """Test with all possibilities set"""
        os.environ['MONGOHQ_URL'] = self.mongohq
        os.environ['MONGOLAB_URI'] = self.mongolab

        connection = mongoify()

        self.assertEqual(connection, self.mongohq)

    def test_mongohq_trumps_default(self):
        """Test using MONGOHQ_URL with a default"""
        os.environ['MONGOHQ_URL'] = self.mongohq

        connection = mongoify(default=self.localhost)

        self.assertEqual(connection, self.mongohq)

    def test_mongolab(self):
        """Test using MONGOLAB_URI"""
        os.environ['MONGOLAB_URI'] = self.mongolab

        connection = mongoify()

        self.assertEqual(connection, self.mongolab)

    def test_mongolab_trumps_default(self):
        """Test using MONGOLAB_URI with a default"""
        os.environ['MONGOLAB_URI'] = self.mongolab

        connection = mongoify(default=self.localhost)

        # Make sure to clean up the setting
        self.assertEqual(connection, self.mongolab)

if __name__ == '__main__':
    unittest.main()
