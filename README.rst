PyCon UK 2016 website
=====================

.. image:: https://travis-ci.org/PyconUK/2016.pyconuk.org.svg?branch=master
       :target: https://travis-ci.org/PyconUK/2016.pyconuk.org

This is the website for PyCon UK. It is hosted via GitHub Pages and will be available at http://pyconuk.org/.

If you have a suggestion to make, please feel free to create an issue_.

We welcome pull requests for improvements! (Please see CONTRIBUTING.rst_ for details.)


Development
~~~~~~~~~~~

This site uses django-amber_. To install django-amber and other dependencies, run ``pip install -r requirements.txt``.  django-amber is only known to work with Python 3.5.

You must also install `less <https://www.npmjs.com/package/less>`_, and ensure that `lessc` is available in your PATH.

django-amber builds the site by assembling several components:

* Pages are found in ``pages/``.  News articles are in ``news/``.  Other types of content may be added later.  Pages may be HTML or Markdown_, and contain some YAML metadata.  Look at existing pages for examples.
* Static files are found in ``media/``.
* Django template for all pages are found in ``templates/``

To build the site, run ``python manage.py buildsite``. This pulls together all the components into a set of HTML files in ``output/``.

Alternatively, if you run ``python manage.py serve``, django-amber will build the site, serve the built site on port 8000, and watch for changes.

You can test that the site contains no broken links and that the conference name is capitalised correctly (hint, it's "PyCon UK") by running ``make test``.

Travis will test branches, and branches won't get merged without review and passing tests, so dive right in!


Deployment
~~~~~~~~~~

The site is hosted as a Project Page on GitHub Pages, and so it is the ``gh-pages`` branch of the repository that gets served.  django-amber generates the site in the ``output/`` directory, and Travis is configured to push any changes to the ``output/`` directory to this branch.  See ``deploy.sh`` for details.

This should be done automatically by Travis after it has built the ``master`` branch, but in case this does not happen, somebody with commit access to the repository can run ``make deploy``.

When setting up Travis to run this initially you must provide an OAuth token for authentication in the ``GH_TOKEN`` env var.  To do this create a `Personal Access Token on GitHub <https://github.com/settings/tokens>`_ then create the ``GH_TOKEN`` key pair on the `Travis settings page <https://travis-ci.org/PyconUK/2016.pyconuk.org/settings>`_.

Note: this is tied to a single user on GitHub, however any other GitHub user with valid permissions can replace the key on Travis.

.. _django-amber: https://github.com/inglesp/django-amber
.. _Markdown: https://pythonhosted.org/Markdown/
.. _issue: https://github.com/PyconUK/2016.pyconuk.org/issues
.. _CONTRIBUTING.rst: ./CONTRIBUTING.rst
