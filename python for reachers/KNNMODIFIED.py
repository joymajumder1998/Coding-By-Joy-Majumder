from sklearn import datasets

irish=datasets.load_iris()
predictors=irish.data[: , :2]
outcomes=irish.target