========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |appveyor| |requires|
        | |codecov|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|
.. |docs| image:: https://readthedocs.org/projects/python-uzbek-stemmer/badge/?style=flat
    :target: https://python-uzbek-stemmer.readthedocs.io/
    :alt: Documentation Status

.. |travis| image:: https://api.travis-ci.com/SanatbekMatlatipov/python-uzbek-stemmer.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.com/github/SanatbekMatlatipov/python-uzbek-stemmer

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/SanatbekMatlatipov/python-uzbek-stemmer?branch=master&svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/SanatbekMatlatipov/python-uzbek-stemmer

.. |requires| image:: https://requires.io/github/SanatbekMatlatipov/python-uzbek-stemmer/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/SanatbekMatlatipov/python-uzbek-stemmer/requirements/?branch=master

.. |codecov| image:: https://codecov.io/gh/SanatbekMatlatipov/python-uzbek-stemmer/branch/master/graphs/badge.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/SanatbekMatlatipov/python-uzbek-stemmer

.. |version| image:: https://img.shields.io/pypi/v/uzbek-stemmer.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/uzbek-stemmer

.. |wheel| image:: https://img.shields.io/pypi/wheel/uzbek-stemmer.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/uzbek-stemmer

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/uzbek-stemmer.svg
    :alt: Supported versions
    :target: https://pypi.org/project/uzbek-stemmer

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/uzbek-stemmer.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/uzbek-stemmer

.. |commits-since| image:: https://img.shields.io/github/commits-since/SanatbekMatlatipov/python-uzbek-stemmer/v0.0.1.svg
    :alt: Commits since latest release
    :target: https://github.com/SanatbekMatlatipov/python-uzbek-stemmer/compare/v0.0.1...master



.. end-badges

Stemming tool for Uzbek language

* Free software: Apache Software License 2.0

Installation
============

::

    pip install uzbek-stemmer

You can also install the in-development version with::

    pip install https://github.com/SanatbekMatlatipov/python-uzbek-stemmer/archive/master.zip


Documentation
=============


https://uzbek-stemmer.readthedocs.io/


Development
===========

To run all the tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
