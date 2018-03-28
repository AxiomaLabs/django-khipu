# !/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

version = '2017.10.20'

setup(
    name='django-khipu',
    version=version,
    description='Aplicación para integrar Khipu en Django',
    author='FyF',
    author_email="hi@misalabs.com",
    url='https://bitbucket.org/startcodecl/khipu',
    license='MIT license',
    platforms=['any'],
    packages=find_packages(),
    install_requires=[
        'requests>=2.5.3',
    ],
    classifiers=[
        "Framework :: Django",
        "Environment :: Web Environment",
        "Programming Language :: Python",
        "Topic :: Utilities",
    ],
    include_package_data=True,
    zip_safe=False,
)
