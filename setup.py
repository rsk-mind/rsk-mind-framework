#!/usr/bin/env python
from distutils.core import setup

__version__ = "0.1.1"

setup(
    name='rsk_mind',
    version=__version__,
    description='Framework for machine learning platform',
    keywords='machine learning deep learning',
    url='git@bitbucket.org:rasarmy/fraud-backend.git',
    author='RSK Mind',
    author_email='',
    license='MIT',
    packages=['rsk_mind', 'rsk_mind.engine', 'rsk_mind.datasource',
              'rsk_mind.classifier', 'rsk_mind.transformer',
              'rsk_mind.filter', 'rsk_mind.dataset'],
    # dependent packages
    install_requires=[
            'numpy',
            'scipy',
            'xgboost==0.4a30',
            'geoip2',
            'scikit-learn'
    ],
    extras_require={
            'docs': ['sphinx']
    },
    zip_safe=False)
