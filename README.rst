PyCon UK 2016 website
=====================

.. image:: https://travis-ci.org/PyconUK/2016.pyconuk.org.svg?branch=master
       :target: https://travis-ci.org/PyconUK/2016.pyconuk.org

This is the website for PyCon UK. It is hosted via GitHub Pages and will be available at http://pyconuk.org/.

If you have a suggestion to make, please feel free to create an issue_.

We welcome pull requests for improvements! (Please see CONTRIBUTING.rst_ for details.)


Development
~~~~~~~~~~~
This site uses wok_.  To install wok and other dendencies, run ``pip install -r requirements.txt``.

wok builds the site by assembling several components:

* Pages are found in ``content/``.  Pages may be HTML, Markdown_ or reStructuredText_, and contain some YAML metadata.
* Static files are found in ``media/``.
* A jinja2_ template for all the pages is found in ``templates/default.html``

To build the site, run ``make build``.  This will pull together all the componenents into a set of HTML files in ``output/``.

Windows users: you need to run the (extensionless) ``wok`` script in c:/pythonxx/scripts. eg ``py -2 c:\python27\scripts\wok``.

Alternatively, if you run ``make serve``, wok will build the site, serve the built site on port 8000, and watch for changes.

Windows users: you need to run the (extensionless) ``wok`` script with the --serve parameter in c:/pythonxx/scripts. eg ``py -2 c:\python27\scripts\wok --serve``.

You can test that the site contains no broken links and that the conference name is capitalised correctly (hint, it's "PyCon UK") by running ``make test``.

Travis will test branches, and branches won't get merged without review and passing tests, so dive right in!


Deployment
~~~~~~~~~~

The site is hosted as a Project Page on GitHub Pages, and so it is the ``gh-pages`` branch of the repository that gets served.  wok generates the site in the ``output/`` directory, and Travis is configured to push any changes to the ``output/`` directory to this branch.  See ``deploy.sh`` for details.

This should be done automatically by Travis after it has built the ``master`` branch, but in case this does not happen, somebody with commit access to the repository can run ``make deploy``.

.. _wok: http://wok.mythmon.com/
.. _Markdown: https://pythonhosted.org/Markdown/
.. _reStructuredText: http://docutils.sourceforge.net/rst.html
.. _jinja2: http://jinja.pocoo.org/
.. _issue: https://github.com/PyconUK/2016.pyconuk.org/issues
.. _CONTRIBUTING.rst: ./CONTRIBUTING.rst
