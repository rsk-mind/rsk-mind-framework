# RSK Mind Framework
[![codecov](https://codecov.io/gh/rsk-mind/rsk-mind-framework/branch/master/graph/badge.svg)](https://codecov.io/gh/rsk-mind/rsk-mind-framework)
[![Build Status](https://travis-ci.org/rsk-mind/rsk-mind-framework.svg?branch=master)](https://travis-ci.org/rsk-mind/rsk-mind-framework)
[![Packagist](https://img.shields.io/packagist/l/doctrine/orm.svg?maxAge=2592000)]()

General propose framework for agile building of a data mining services. With this
framework a developer with low effort can deploy a machine learning services.


Framework has three independent modules,

1. **Transformation** Processing and augmenting our dataset.
2. **Analytics** Get information about the dataset.
3. **Training** Training of a new model for prediction or classification.
4. **Prediction - Classification** Get the result for the instance via a REST API.

## Transformation

You can add a new feature on dataset, drop a feature and transform a feature.

1. Combine two or more feature on new features, etc (a, b, c) -> (d, e).
2. Transform feature on new format, etc (a) -> (1/a).
3. From a feature get more derivative ones, etc (a) -> (a1, a2, a3).
4. Drop a feature.
5. ~~Join two dataset on a foreign key.~~

## Analytics

## Training

## Predicting
