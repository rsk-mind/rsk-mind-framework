#!/usr/bin/env python
from setuptools import setup, find_packages

__version__ = "0.1.1"

setup(
    name='RSK Mind',
    version=__version__,
    description='Framework for machine learning platform',
    keywords='machine learning deep learning',
    url='git@bitbucket.org:rasarmy/framework.git',
    author='RSK Project',
    author_email='admin@rsk-project.com',
    license='MIT',
    scripts=['rsk_mind/bin/rskmind-admin.py'],
    entry_points={'console_scripts': [
        'rskmind-admin = rskmind.core.management:execute_from_command_line',
    ]},
    include_package_data=True,
    packages=find_packages(exclude=('tests', 'tests.*', 'doc', 'tests.*')),
    install_requires=[
            'xgboost==0.4a30',
            'geoip2',
            'scikit-learn',
            'scipy',
            'Jinja2',
            'pandas',
            'numpy'
    ],
    extras_require={
            'docs': ['sphinx'],
            'tests': ['nose']
    },
    zip_safe=False
)
