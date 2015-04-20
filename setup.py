# coding=utf-8

# Copyright (C) 2013-2015 David R. MacIver (david@drmaciver.com)

# This file is part of Hypothesis (https://github.com/DRMacIver/hypothesis)

# This Source Code Form is subject to the terms of the Mozilla Public License,
# v. 2.0. If a copy of the MPL was not distributed with this file, You can
# obtain one at http://mozilla.org/MPL/2.0/.

# END HEADER

from setuptools.command.test import test as TestCommand
from setuptools import find_packages
import sys
import os

import vsc.install.shared_setup as shared_setup

V = '1.2.1'

shared_setup.SHARED_TARGET.update({
    'url': 'https://pypi.python.org/pypi/hypothesis',
    'download_url': ('https://pypi.python.org/packages/source/h/hypothesis/'
                     'hypothesis-%s.tar.gz#md5=5070d89fc001a1055133eb8f75b75080' % (V,))
})

def local_file(name):
    return os.path.join(os.path.dirname(__file__), name)

SOURCE = local_file("src")
README = local_file("README.rst")


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = ["tests"]
        self.test_suite = True

    def run_tests(self):
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)

PACKAGE = {
    'name': 'hypothesis',
    'version': V,
    'author': ['David R. MacIver'],
    'author_email': 'david@drmaciver.com',
    'packages': find_packages(SOURCE),
    'package_dir': {"": SOURCE},
    'url': 'https://github.com/DRMacIver/hypothesis',
    'license': 'MPL v2',
    'description': 'A library for property based testing',
    'zip_safe': False,
    'classifiers': [
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
        "Operating System :: Unix",
        "Operating System :: POSIX",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development :: Testing",
    ],
    'long_description': open(README).read(),
    'tests_require': [
        'pytest', 'pytest-rerunfailures', 'pytest-faulthandler', 'flake8'],
    'cmdclass': {'test': PyTest},
}

PACKAGE['provides'] =  ['python-hypothesis = %s' % (V,)]

if __name__ == '__main__':
    shared_setup.action_target(PACKAGE)
