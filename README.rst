=============================================================
django-heroku-mongoify: Friendly MongoDB for Django on Heroku
=============================================================

.. image:: https://secure.travis-ci.org/dirn/django-heroku-mongoify.png?branch=master

A user-friendly method to configure Django projects on Heroku to use MongoDB.

Inspired by the work of `Randall Degges`_.

.. _Randall Degges: https://github.com/rdegges


Usage
=====

Place this code into your project's settings.py::

    from mongoify import mongoify
    from pymongo import MongoClient
    db = MongoClient(mongoify(default='mongodb://localhost/test')['default'])

Full documentation can be found on `Read the Docs`_.

.. _Read the Docs: http://readthedocs.org/docs/django-heroku-mongoify/en/latest/


Installation
============

To install the latest version of django-heroku-mongoify::

    $ pip install django-heroku-mongoify

or, if you must::

    $ easy_install django-heroku-mongoify

To install the latest development version::

    $ git clone git@github.com:dirn/django-heroku-mongoify.git
    $ cd django-heroku-mongoify
    $ python setup.py install


Changelog
=========

- 0.2.0:
  - THIS RELEASE IS NOT BACKWARDS COMPATIBLE
  - ``mongoify()`` now returns a ``dict`` of all URIs found in the
  environment settings.

- 0.1.0:
  - Initial release
