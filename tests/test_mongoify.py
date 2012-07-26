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
        if 'MONGOHQ_URL' in os.environ:
            tmp = os.environ['MONGOHQ_URL']
        else:
            tmp = None

        os.environ['MONGOHQ_URL'] = self.mongohq

        connection = mongoify()

        # Make sure to clean up the setting
        if tmp is None:
            del os.environ['MONGOHQ_URL']
        else:
            os.environ['MONGOHQ_URL'] = tmp

        self.assertEqual(connection, self.mongohq)

    def test_mongohq_trumps_all(self):
        """Test with all possibilities set"""
        if 'MONGOHQ_URL' in os.environ:
            tmp1 = os.environ['MONGOHQ_URL']
        else:
            tmp1 = None
        if 'MONGOLAB_URI' in os.environ:
            tmp2 = os.environ['MONGOLAB_URI']
        else:
            tmp2 = None

        os.environ['MONGOHQ_URL'] = self.mongohq
        os.environ['MONGOLAB_URI'] = self.mongolab

        connection = mongoify()

        # Make sure to clean up the settings
        if tmp1 is None:
            del os.environ['MONGOHQ_URL']
        else:
            os.environ['MONGOHQ_URL'] = tmp1
        if tmp2 is None:
            del os.environ['MONGOLAB_URI']
        else:
            os.environ['MONGOLAB_URI'] = tmp2

        self.assertEqual(connection, self.mongohq)

    def test_mongohq_trumps_default(self):
        """Test using MONGOHQ_URL with a default"""
        if 'MONGOHQ_URL' in os.environ:
            tmp = os.environ['MONGOHQ_URL']
        else:
            tmp = None

        os.environ['MONGOHQ_URL'] = self.mongohq

        connection = mongoify(default=self.localhost)

        # Make sure to clean up the setting
        if tmp is None:
            del os.environ['MONGOHQ_URL']
        else:
            os.environ['MONGOHQ_URL'] = tmp

        self.assertEqual(connection, self.mongohq)

    def test_mongolab(self):
        """Test using MONGOLAB_URI"""
        if 'MONGOLAB_URI' in os.environ:
            tmp = os.environ['MONGOLAB_URI']
        else:
            tmp = None

        os.environ['MONGOLAB_URI'] = self.mongolab

        connection = mongoify()

        # Make sure to clean up the setting
        if tmp is None:
            del os.environ['MONGOLAB_URI']
        else:
            os.environ['MONGOLAB_URI'] = tmp

        self.assertEqual(connection, self.mongolab)

    def test_mongolab_trumps_default(self):
        """Test using MONGOLAB_URI with a default"""
        if 'MONGOLAB_URI' in os.environ:
            tmp = os.environ['MONGOLAB_URI']
        else:
            tmp = None

        os.environ['MONGOLAB_URI'] = self.mongolab

        connection = mongoify(default=self.localhost)

        # Make sure to clean up the setting
        if tmp is None:
            del os.environ['MONGOLAB_URI']
        else:
            os.environ['MONGOLAB_URI'] = tmp

        self.assertEqual(connection, self.mongolab)

if __name__ == '__main__':
    unittest.main()
