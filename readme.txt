Assignment 2
Group 58 :  Chavisha Arora (2018136)
Team Name : Corona

----------
HOW TO RUN
----------

Extract all the files in the same folder and then enter the following command to run main.py and generate result.csv. This is the main script for our prediction model.

-> py main.py

Extract all the files in the same folder and then enter the following command to run internal_testing.py. This script is used to test our prediction model.

-> py internal_testing.py

-----------------
PACKAGES REQUIRED
-----------------

- scikit-learn
- pandas



--------------
IMPORTANT NOTE
--------------

1) The script requires the train.csv and the test.csv file to be in the same folder.
2) Running main.py produces an output file called result.csv.
3) Running internal_testing.py shows the prediction score of the model with the train-test split data.
4) Since the machine learning model used in the script has a random state, the output may vary every time the script is run.
5) The output may vary slightly from the predictions given.
6) result1.csv, result2.csv, result3.csv are the predictions that were uploaded on Kaggle and used for the final scoring.


-------
DETAILS
-------
1) The training and test data is extracted from the file train.csv and test.csv using the pandas library.
2) For each sequence, the amino acid composition is calculated. Only the count of each amino acid in the given sequence is calculated, not the percentage count.
3) Since there are 20 amino acids, for each sequence we thus calculate a list of length 20 to be used as the input feature for our model.
4) Feature selection is done on the given training data using a pipeline and the SelectFromModel() function provided in the sklearn library.
5) SelectFromModel() function is provided as parameter a LinearSVC model with the parameters ( penalty="l1" , dual = False ) to do feature selection.
6) An ExtraTreesClassifier model is trained using the training data filtered using the feature selection.
7) The n_estimators parameter of the ExtraTreesClassifier model is set to 400. This value was found by hit and trial done on internal_testing.py. The purpose of this script was to create a train test split (70-30) in order to test our model with different features and values of n_estimator parameter.
8) After the model is fitted with the training and testing data and run, the prediction is stored in a list val_y.
9) A dataframe which stores the final prediction is created as per the format given in sample.csv. This is stored in the variable, result.
10) The output file result.csv is generated from the dataframe result using the pandas library.