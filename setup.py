#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

import setuptools.command.egg_info as egg_info_cmd
from setuptools import setup, find_packages

SETUP_DIR = os.path.dirname(__file__)
README = os.path.join(SETUP_DIR, 'README.rst')

try:
    import gittaggers
    tagger = gittaggers.EggInfoFromGit
except ImportError:
    tagger = egg_info_cmd.egg_info

needs_pytest = {'pytest', 'test', 'ptr'}.intersection(sys.argv)
pytest_runner = ['pytest-runner'] if needs_pytest else []

if os.path.exists("requirements.txt"):
    requirements = [
        r for r in open("requirements.txt").read().split("\n") if ";" not in r]
else:
    # In tox, it will cover them anyway.
    requirements = []

install_requires = [
    'setuptools',
    'requests >= 1.0',
    'ruamel.yaml >= 0.12.4, <= 0.15.51',
    'rdflib >= 4.2.2, < 4.3.0',
    'rdflib-jsonld >= 0.3.0, < 0.5.0',
    'mistune >= 0.7.3, < 0.8',
    'CacheControl >= 0.11.7, < 0.12',
    'lockfile >= 0.9',
    'six >= 1.8.0']

extras_require={
    ':python_version<"3"': ['avro == 1.8.1'],
    ':python_version<"3.7"': ['typing >= 3.6.4'],
    ':python_version>="3"': ['future', 'avro-cwl == 1.8.4']  # fork of avro for working with python3
}

setup(name='schema-salad',
      version='2.7',  # update the VERSION prefix in the Makefile as well 🙂
      description='Schema Annotations for Linked Avro Data (SALAD)',
      long_description=open(README).read(),
      author='Common workflow language working group',
      author_email='common-workflow-language@googlegroups.com',
      url="https://github.com/common-workflow-language/common-workflow-language",
      download_url="https://github.com/common-workflow-language/common-workflow-language",
      license='Apache 2.0',
      setup_requires=[] + pytest_runner,
      packages=["schema_salad", "schema_salad.tests"],
      package_data={'schema_salad': ['metaschema/*']},
      include_package_data=True,
      install_requires=install_requires,
      extras_require=extras_require,
      test_suite='tests',
      tests_require=['pytest'],
      entry_points={
          'console_scripts': ["schema-salad-tool=schema_salad.main:main", "schema-salad-doc=schema_salad.makedoc:main"]
      },
      zip_safe=True,
      cmdclass={'egg_info': tagger},
      classifiers=[
          "Environment :: Console",
          "Intended Audience :: Science/Research",
          "License :: OSI Approved :: Apache Software License",
          "Operating System :: POSIX",
          "Operating System :: MacOS :: MacOS X",
          "Operating System :: Microsoft :: Windows",
          "Development Status :: 5 - Production/Stable",
          "Programming Language :: Python :: 2.7",
          "Programming Language :: Python :: 3.4",
          "Programming Language :: Python :: 3.5",
          "Programming Language :: Python :: 3.6",
          "Programming Language :: Python :: 3.7"
      ]
      )
