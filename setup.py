#!/usr/bin/env python
# -*- coding: utf-8 -*-
from distutils.core import setup
from sys import version


if version < '2.7':
    raise NotImplementedError("Echo requires Python 2.7.* or above.")


setup(
    name='Echo',
    url='https://github.com/spitfire-sidra/Echo',
    version='0.0.1.alpha',
    author='Amo Chen',
    author_email='spitfire.sidra@gmail.com',
    packages=['Echo',],
    license='License.txt',
    description='Really simple api response maker for dummies',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Topic :: Utilities',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ]
)
