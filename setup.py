#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Setup for Python package.

---
This file is part of azimutt-containers-density
Copyright (c) 2020 Deepnox.
Distributed under the MIT License (license terms are at http://opensource.org/licenses/MIT).
---
"""

import pip
import os, sys
from setuptools import setup, find_packages

sys.path.insert(0, os.path.dirname(__file__))

from packaging import CONFIGURATION

links = []
requires = []

requirements = pip.req.parse_requirements(os.path.join(os.path.dirname(__file__), 'requirements.txt'), session=pip.download.PipSession())

download_url = 'https://github.com/azimutt-io/azimutt-containers-density/archive/v%s.tar.gz' % CONFIGURATION['version']

for item in requirements:
    # we want to handle package names and also repo urls
    if getattr(item, 'url', None):  # older pip has url
        links.append(str(item.url))
    if getattr(item, 'link', None):  # newer pip has link
        links.append(str(item.link))
    if item.req:
        requires.append(str(item.req))

setup(name='%s' % (CONFIGURATION['name']),
      version=CONFIGURATION['version'],
      description=CONFIGURATION['description'],
      long_description='Please refer to Github README: http://github.com/azimutt-io/azimutt-containers-density/#readme',
      url='http://github.com/azimutt-io/azimutt-containers-density',
      author=CONFIGURATION['author'],
      author_email=CONFIGURATION['email'],
      license=license,
      packages=find_packages('src'),
      package_dir={'': 'src'},
      namespace_packages=['azimutt', 'azimutt.containers_density'],
      zip_safe=False,
      install_requires=requires,
      include_package_data=True,
      python_requires=', '.join((
          '>=3.5',
          '!=3.0.*',
          '!=3.1.*',
          '!=3.2.*',
          '!=3.3.*',
      )),
      # extras_require={
      #    'docs': ['Sphinx', 'repoze.sphinx.autointerface'],
      #    'test': tests_require,
      #    'testing': testing_extras,
      # },
      # features=features,
      test_suite='test.test_suite',
      keywords=['azimutt', 'azimutt.io', 'density', 'testing', 'containers', 'docker'],
      classifiers=[
          'Development Status :: 3 - %s' % CONFIGURATION['status'],
          'Topic :: Software Development :: Libraries :: Application Frameworks',
          'License :: OSI Approved :: %s License' % CONFIGURATION['license'],
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          ],
      download_url=download_url,
      )
