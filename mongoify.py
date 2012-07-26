# -*- coding: utf-8 -*-

""" Friendly MongoDB for Django on Heroku """

import os

MONGO_URLS = (
    'MONGOHQ_URL',
    'MONGOLAB_URI',
)


def mongoify(default=None):
    """Returns URL based on environment settings.

    :param default: A URL for a MongoDB database.
    :type default: str.
    :returns: dict -- A URL that can be used for a ``pymongo.Connection``.

    Supported providers:

    - MongoHQ (MONGOHQ_URL)
    - MongoLab (MONGOLAB_URI)

    Other MongoDB hosts can be utilized by passing the URL as ``default``::

        mongoify(default='mongodb://localhost')

    .. versionadded:: 0.1.0
    """
    url = None
    # If any of the supported URL environment variables exist, use the first
    # one defined in `MONGO_URLS`.
    urls = (os.getenv(url) for url in MONGO_URLS if os.getenv(url))
    for url in urls:
        break

    # If no supported URLs exist and a default is provided, use it.
    if not url and default is not None:
        url = default

    return url
