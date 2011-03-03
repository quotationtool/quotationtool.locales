# -*- coding: utf-8 -*-
"""Setup for quotationtool.locales package

$Id$
"""
from setuptools import setup, find_packages
import os

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

name='quotationtool.locales'

setup(
    name = name,
    version='0.1.0',
    description="quotationtool.org UI translations",
    long_description=(
        read('README')
        + '\n' +
        'Detailed Documentation\n'
        '**********************\n'
        + '\n' +
        read('src', 'quotationtool', 'locales', 'README.txt')
        + '\n' +
        'Download\n'
        '********\n'
        ),
    keywords='quotationtool',
    author=u"Christian Lueck",
    author_email='cluecksbox@googlemail.com',
    url='',
    license='ZPL 2.1',
    # Get more from http://www.python.org/pypi?%3Aaction=list_classifiers
    classifiers=['Programming Language :: Python',
                 'Environment :: Web Environment',
                 'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
                 'Framework :: BlueBream',
                 ],
    packages = find_packages('src'),
    package_dir = {'': 'src'},
    include_package_data=True,
    zip_safe=False,
    install_requires = [
        'setuptools',
        ],
    extras_require = dict(
        i18n = [
            'z3c.recipe.i18n',
            'z3c.csvvocabulary',
            'zope.component',
            'zope.i18n',
            'zope.app.appsetup',
            'zope.app.applicationcontrol',

            # quotationtool
            'quotationtool.site',
            'quotationtool.security',
            'quotationtool.renderer',
            'quotationtool.relation',
            'quotationtool.skin',
            'quotationtool.search',
            'quotationtool.bibliography',
            'quotationtool.biblatex',
            'quotationtool.figuresng',
            'quotationtool.commentary',
            'quotationtool.categorization',
            'quotationtool.user',
            'quotationtool.tinymce',
            ],
        ),

    )
