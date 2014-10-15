# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from plone.theme.interfaces import IDefaultPloneLayer
from zope.interface import Interface


class IPloneintranetDocconvClientLayer(IDefaultPloneLayer):
    """Marker interface that defines a Zope 3 browser layer."""


class IPreviewFetcher(Interface):
    """ Adapter that fetches preview images and pdf version for an object from
    the docconv service """

    def __call__():
        """ fetches everything and stores it in annotations on the object """
