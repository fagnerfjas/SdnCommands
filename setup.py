#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Auth: Fagner
# V = 1.0
##
## Arquivo de configuração da interface CLI Python 
## Lib Click http://click.pocoo.org/5 
## 2017

from setuptools import setup, find_packages

setup(
    name='Sdn Commands',
    version='0.1',
    packages=find_packages(),
	include_package_data=True,
    install_requires=[
        'Click',
    ],
    entry_points={
		'console_scripts': [
			'sdn=src.sdn:cli',
		]
	},
)
