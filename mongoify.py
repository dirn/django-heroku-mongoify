# -*- coding: utf-8 -*-

""" Friendly MongoDB for Django on Heroku """

import os

__all__ = ('mongoify',)


def mongoify(default=None):
    """Returns a dictionary of URIs based on environment settings.

    This method will look for MongoDB URI connection strings in the
    environment settings. It will first check for ``MONGO_URI``. If this
    setting is found, it will be in the result ``dict`` as the
    ``default`` key. The method will then iterate through the
    settings looking for any additional URI connection strings. Any that
    are found will be added to the result ``dict``.

    In the event that ``MONGO_URI`` was not found, the first URI
    connection string encountered will be used as the ``default`` key.
    This URI will appear twice.

    In the event that ``MONGO_URI`` was not found and no other URI
    connection strings were found, the value provided through the
    ``default`` argument will be used as the ``default`` key.

    If ``default`` was no provided and no other URI connection strings
    were found, the ``dict`` will be empty.

    :param default: A connection string URI for a MongoDB database.
    :type default: str.
    :returns: dict -- connection string URIs that can be used with
              ``pymongo.MongoClient``.

    .. versionchanged:: 0.2.0
       ``mongoify()`` now returns a ``dict`` containing all URIs
    .. versionadded:: 0.1.0
    """

    uris = {}

    # If the MONGO_URI key exists in the environment settings, it should
    # be considered the default.
    if 'MONGO_URI' in os.environ:
        uris['default'] = os.environ['MONGO_URI']

    # Loop through all other environment settings and look for URI
    # connection strings. If any are found, add them to the dict.
    for k, v in os.environ.items():
        if v.startswith('mongodb://'):
            if k == 'MONGO_URI':
                continue

            # Make the dictionary key a bit more human friendly. (I
            # totally ripped this off from postgresify, except for the
            # ugly try/excepts, those are mine.)
            key = k.split('_')
            if 'URI' in key:
                key.remove('URI')
            if 'URL' in key:
                key.remove('URL')
            key = '_'.join(key)

            uris[key] = v

            # In the even that MONGO_URI wasn't found, the first URI
            # encountered should be used as the default.
            if 'default' not in uris:
                uris['default'] = v

    # If no URIs exist in the environment settings and a default was
    # provided, use it.
    if not ('default' in uris or default is None):
        uris['default'] = default

    return uris
