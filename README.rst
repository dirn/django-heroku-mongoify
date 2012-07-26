=============================================================
django-heroku-mongoify: Friendly MongoDB for Django on Heroku
=============================================================

A user-friendly method to configure Django projects on Heroku to use MongoDB.

Inspired by the work of `Randall Degges`_.

.. _Randall Degges: https://github.com/rdegges

Usage
=====

Place this code into your project's settings.py::

    from mongoify import mongoify
    from pymongo import Connection
    db = Connection(mongoify(default='mongodb://localhost'))

Full documentation can be found on `Read the Docs`_.

.. _Read the Docs: http://readthedocs.org/docs/django-heroku-mongoify/en/latest/

Installation
============

Installing django-heroku-mongoify is easy::

    pip install django-heroku-mongoify

or download the source and run::

    python setup.py install
