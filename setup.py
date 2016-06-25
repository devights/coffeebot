#!/usr/bin/env python

import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='coffeebot',
    version='0.1',
    packages=['bot_manager'],
    include_package_data=True,
    install_requires=[
        'setuptools',
        'django<2.0',
        'nameparser>=0.2.8',
        'slacker',
        'websocket-client',
        'python-dateutil',
        'django-compressor<2.0'
    ],
    license='Apache License, Version 2.0',
    description='An application that manages Slack Bots',
    long_description=README,
    url='https://github.com/devights/coffeebot',
    author='Stephen De Vight',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
    ],
)
