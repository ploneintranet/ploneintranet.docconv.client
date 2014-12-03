# -*- coding: utf-8 -*-
"""Installer for the ploneintranet.docconv.client package."""

from setuptools import find_packages
from setuptools import setup

import os


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

long_description = \
    read('README.rst') + \
    read('docs', 'CHANGELOG.rst') + \
    read('docs', 'LICENSE.rst')

setup(
    name='ploneintranet.docconv.client',
    version='0.1',
    description="Generate previews for office documents",
    long_description=long_description,
    # Get more from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
    ],
    keywords='office,preview,thumbnail',
    author='syslab.com',
    author_email='info@syslab.com',
    url='http://pypi.python.org/pypi/ploneintranet.docconv.client',
    license='BSD',
    packages=find_packages('src', exclude=['ez_setup']),
    namespace_packages=['ploneintranet', 'ploneintranet.docconv', ],
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'BeautifulSoup',
        'five.grok',
        'five.pt',
        'Pillow',
        'Plone',
        'plone.api',
        'plone.app.async',
        'plone.app.registry',
        'setuptools',
        'z3c.jbot',
    ],
    extras_require={
        'test': [
            'mock',
            'plone.app.contenttypes',
            'plone.app.testing',
            'unittest2',
        ],
        'develop': [
            'coverage',
            'flake8',
            'jarn.mkrelease',
            'niteoweb.loginas',
            'plone.app.debugtoolbar',
            'plone.reload',
            'Products.Clouseau',
            'Products.DocFinderTab',
            'Products.PDBDebugMode',
            'Products.PrintingMailHost',
            'Sphinx',
            'zest.releaser',
            'zptlint',
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
