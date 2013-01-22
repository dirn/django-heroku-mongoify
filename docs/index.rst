======================
django-heroku-mongoify
======================

django-heroku-mongoify provides a user-friendly method to configure Django
projects on Heroku to use MongoDB.

Inspired by the work of `Randall Degges`_.

.. _Randall Degges: https://github.com/rdegges

.. toctree::
   :maxdepth: 2


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


Usage
=====

In settings.py:

.. code-block:: python

    from mongoify import mongoify
    from pymongo import MongoClient
    db = MongoClient(mongoify(default='mongodb://localhost/test')['default'])


API
===

.. automodule:: mongoify
   :members:


Further Reading
===============

More information about URI connection strings can be found in the
`MongoDB Docs`_.

.. _MongoDB Docs: http://docs.mongodb.org/manual/reference/connection-string/


Changelog
=========

- 0.2.0:
  - THIS RELEASE IS NOT BACKWARDS COMPATIBLE
  - ``mongoify()`` now returns a ``dict`` of all URIs found in the
  environment settings.

- 0.1.0:
  - Initial release


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
