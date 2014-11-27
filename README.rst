
.. image:: https://api.travis-ci.org/ploneintranet/ploneintranet.docconv.client.png
   :alt: Build Status
   :target: https://travis-ci.org/ploneintranet/ploneintranet.docconv.client

============================
ploneintranet.docconv.client
============================

Generate previews for office documents

* `Source code @ GitHub <https://github.com/ploneintranet/ploneintranet.docconv.client>`_
* `Releases @ PyPI <http://pypi.python.org/pypi/ploneintranet.docconv.client>`_
* `Documentation @ ReadTheDocs <http://ploneintranetdocconvclient.readthedocs.org>`_
* `Continuous Integration @ Travis-CI <http://travis-ci.org/ploneintranet/ploneintranet.docconv.client>`_

How it works
============

When a content object is added, an event handler (see handlers.py) triggers the preview generation. If plone.app.async is set up, the previews are generated asynchronously. The process relies on an external server that is running `slc.docconv <https://github.com/syslabcom/slc.docconv>`_. Upon completion the previews are stored in annotations on the object. In addition to the preview images a PDF version of the object is generated and stored. There are views in view.py that allow the previews and pdfs to be displayed.


Installation
============

To install `ploneintranet.docconv.client` you simply add ``ploneintranet.docconv.client``
to the list of eggs in your buildout, run buildout and restart Plone.
Then, install `ploneintranet.docconv.client` using the Add-ons control panel.


Configuration
=============

Currently most of the configuration is static (config.py). The plan is to replace this by a proper TTW configuration. The URL of the external slc.docconv server is currently stored in site_properties. This could also be moved to e.g. plone.registry.


Copyright (c) Plone Foundation
------------------------------

This package is Copyright (c) Plone Foundation.

Any contribution to this package implies consent and intent to irrevocably transfer all 
copyrights on the code you contribute, to the `Plone Foundation`_, 
under the condition that the code remains under a `OSI-approved license`_.

To contribute, you need to have signed a Plone Foundation `contributor agreement`_.
If you're `listed on Github`_ as a member of the Plone organization, you already signed.

.. _Plone Foundation: https://plone.org/foundation
.. _OSI-approved license: http://opensource.org/licenses
.. _contributor agreement: https://plone.org/foundation/contributors-agreement
.. _listed on Github: https://github.com/orgs/plone/people
