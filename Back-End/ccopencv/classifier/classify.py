

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.externals import joblib
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix


from datamaker import DataMaker


class Classify(object):


    def __init__(self, path_to_train, model_name):
        self.path = path_to_train
        self.model_name = model_name
        dm = DataMaker(self.path)
        dm.makeData()

        train_features = dm.train_features
        train_labels = dm.train_labels

        print('train_features: ',len(dm.train_features))
        print('train_labels:', len(dm.train_labels))

        print('train_label[100]: ', train_labels[100])
        print('train_features[100]: ', train_features[100])

        train_x, test_x, train_y, test_y = self.split_dataset(train_features, train_labels, 0.8)

        self.trained_model = self.random_forest(train_x, train_y)
        self.save_model()

        print(self.trained_model)
        print(self.trained_model.predict([[120.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,  0.0, 0.0]]))
        predictions = self.trained_model.predict(test_x)

        print("Train Accuracy :: ", accuracy_score(train_y, self.trained_model.predict(train_x)))
        print("Test Accuracy  :: ", accuracy_score(test_y, predictions))
        print("Confusion matrix ", confusion_matrix(test_y, predictions))


    def split_dataset(self, feature, labels, train_percentage):
        """
        Split the dataset with train_percentage
        :return: train_x, test_x, train_y, test_y
        """
        train_x, test_x, train_y, test_y = train_test_split(feature, labels, train_size=train_percentage)
        return train_x, test_x, train_y, test_y


    def random_forest(self, train_x, train_y):
        """ Train model using Random Forest Classifier """
        clf = RandomForestClassifier(max_depth=10, random_state=0)
        clf.fit(train_x, train_y)
        return clf

    def save_model(self):
        """ Save model so it can be loaded later """
        joblib.dump(self.trained_model , self.model_name)


if __name__ == '__main__':
    Classify('training-set1/','rTree_trained_model.pkl' )
    Classify('training-set2/', 'rTree_trained_model_ps.pkl')

