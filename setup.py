# -*- coding: utf-8 -*-
import os
import re
import sys

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', 'Arguments to pass to py.test')]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)

here = os.path.dirname(__file__)
version_regex = re.compile(r".*__version__ = '(.*?)'", re.S)
version_script = os.path.join(here, 'src', 'sphinxjp',
                              'themes', 'gopher', '__init__.py')
version = version_regex.match(open(version_script, 'r').read()).group(1)


install_requires = [
    'Sphinx',
]

tests_require = [
    'pytest-cov',
    'pytest',
    'mock',
]

long_description = '\n'.join([
    open(os.path.join("README.rst")).read(),
    open(os.path.join("src", "AUTHORS.txt")).read(),
    open(os.path.join("src", "HISTORY.txt")).read(),
])

classifiers = [
    "Development Status :: 4 - Beta",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python",
    "Programming Language :: Python :: 2",
    "Programming Language :: Python :: 2.7",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.3",
    "Programming Language :: Python :: 3.4",
    "Programming Language :: Python :: 3.5",
    "Programming Language :: Python :: 3.6",
    "Framework :: Sphinx",
    "Framework :: Sphinx :: Extension",
    "Framework :: Sphinx :: Theme",
    "Topic :: Software Development",
    "Topic :: Software Development :: Documentation",
    "Topic :: Text Processing :: Markup",
]

description = 'A sphinx theme for generate gotalk style presentation. #sphinxjp'

setup(
    name='sphinxjp.themes.gopher',
    version=version,
    description=description,
    long_description=long_description,
    classifiers=classifiers,
    keywords=['sphinx', 'reStructuredText', 'theme', 'presentation'],
    author='tell-k',
    author_email='ffk2005 at gmail dot com',
    url='https://github.com/tell-k/sphinxjp.themes.gopher',
    license='MIT',
    namespace_packages=['sphinxjp', 'sphinxjp.themes'],
    packages=find_packages('src', exclude=['tests']),
    package_dir={'': 'src'},
    cmdclass={'test': PyTest},
    include_package_data=True,
    install_requires=install_requires,
    tests_require=tests_require,
    entry_points="""
        [sphinx_themes]
        path = sphinxjp.themes.gopher:get_path

        [sphinx_directives]
        setup = sphinxjp.themes.gopher:setup
    """,
    zip_safe=False
)
