#!/usr/bin/env python

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

readme = open('README.rst').read()

# doclink = """
# Documentation
# -------------
#
# The full documentation is at http://stowage.rtfd.org."""
# history = open('HISTORY.rst').read().replace('.. :changelog:', '')
doclink = ''
history = ''

setup(
    name='stowage',
    version='0.1.0',
    description='Stow-like designed for keeping dotfiles under version control, written in python',
    long_description=readme + '\n\n' + doclink + '\n\n' + history,
    author='michaelb',
    author_email='michaelpb@gmail.com',
    url='https://github.com/michaelpb/stowage',
    packages=[
        'stowage',
    ],
    package_dir={'stowage': 'stowage'},
    include_package_data=True,
    install_requires=[
    ],
    license='GPL3',
    zip_safe=False,
    keywords='stowage',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: PyPy',
        'License :: OSI Approved :: GPL License',
        'License :: OSI Approved :: '
        'GNU General Public License v3 or later (GPLv3+)',
    ],
)
