from rsk_mind.datasource import CSVDatasource

datasource = CSVDatasource('in.csv')
dataset = datasource.read()
dataset.applyTransformations()
datasource = CSVDatasource('out.csv')
datasource.write(dataset)
