# -*- coding: utf-8 -*-
# Copyright (c) 2017 Vincent Bernat
# Licensed under the ISC License

u"""This is a lexer for JunOS configuration files using the pygments engine.
"""

from setuptools import setup

setup(
    name='pygments-junos',
    version='0.0.1',
    description='JunOS Lexer for Pygments',
    long_description=__doc__,
    author='Vincent Bernat',
    author_email='vincent@bernat.im',
    license='ISC',
    keywords='syntax highlighting junos juniper',
    url='http://github.com/vincentbernat/pygments-junos/',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Text Processing',
        'Topic :: Utilities',
    ],
    packages=['junos'],
    install_requires=['Pygments >= 2'],
    include_package_data=False,
    platforms=['any'],
    entry_points={
        'pygments.lexers': [
            'JunosLexer = junos:JunosLexer'
        ],
    },
    zip_safe=False
)
