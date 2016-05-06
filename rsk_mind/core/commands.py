def transformation(setting):
    DATASOURCE = setting.DATASOURCE

    datasource = DATASOURCE['IN']['class'](*DATASOURCE['IN']['params'])
    dataset = datasource.read()

    datasource = DATASOURCE['OUT']['class'](*DATASOURCE['OUT']['params'])
    datasource.write(dataset)
