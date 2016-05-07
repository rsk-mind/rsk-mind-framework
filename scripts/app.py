from rsk_mind.datasource import CSVDatasource

from .settings import *

datasource = CSVDatasource('in.csv')
dataset = datasource.read()
dataset.applyTransformations()
datasource = CSVDatasource('out.csv')
datasource.write(dataset)
