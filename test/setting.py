from rsk_mind.datasource import *
from rsk_mind.classifier import *

from transformer import CustomTransformer

PROJECT_NAME = 'test'

DATASOURCE= {
    'IN' : {
        'class' : CSVDataSource,
        'params' : ('in.csv', )
    },
    'OUT' : {
        'class' : CSVDataSource,
        'params' : ('out.csv', )
    }
}

ANALYSIS = {
    'persist': True,
    'out': 'info.json'
}

TRANSFORMER = CustomTransformer

TRAINING = {
    'algorithms' : [
        {
            'classifier': XGBoostClassifier,
            'parameters' : {
                'bst:max_depth': 7,
                'bst:eta': 0.3,
                'bst:subsample': 0.5,
                'silent': 0,
                'objective': 'binary:logistic',
                'nthread': 4,
                'eval_metric': 'auc'
            },
            'dataset': DATASOURCE['IN']
        }
    ],
    'ensemble': 'max',
    'dataset': DATASOURCE['IN']
}

ENGINE = {

}