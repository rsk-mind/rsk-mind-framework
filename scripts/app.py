from rsk_mind.datasource import CSVDatasource

datasource = CSVDatasource('in.csv')
dataset = datasource.read()
dataset.setTransformer(1)
dataset.applyTransformations()
datasource = CSVDatasource('out.csv')
datasource.write(dataset)
