django-heroku-mongoify 0.1.0
===================================

.. image:: https://secure.travis-ci.org/dirn/django-heroku-mongoify.png?branch=master

django-heroku-mongoify provides a user-friendly method to configure Django
projects on Heroku to use MongoDB.

Inspired by the work of `Randall Degges`_.

.. _Randall Degges: https://github.com/rdegges

.. toctree::
   :maxdepth: 2

Usage
-----

In settings.py::

    from mongoify import mongoify
    from pymongo import Connection
    db = Connection(mongoify(default='mongodb://localhost'))

.. automodule:: mongoify
   :members:

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

