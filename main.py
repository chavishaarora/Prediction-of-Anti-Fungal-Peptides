import pandas as pd
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.feature_selection import SelectFromModel
from sklearn.pipeline import Pipeline
from sklearn.svm import LinearSVC

def split(word):
    return [char for char in word]

# A function that returns a list which stores the  amino_acid composition of a peptide (sequence).
def get_amino_acid_composition(sequence):
    amino_acids = 'ARNDCEQGHILKMFPSTWYV'

    n = len(sequence)
    N = len(amino_acids)
    composition = []
    for i in range(N):
        composition.append(0)

    for i in sequence:

        composition[amino_acids.find(i)] += 1


    return composition


# File path for training data.
file_path_train = './train.csv'

# File path for testing data.
file_path_test = './test.csv'

data_train = pd.read_csv(file_path_train, delimiter=',')
data_test = pd.read_csv(file_path_test, delimiter=',')
sequence_data_train = list(data_train['Sequence'])
sequence_data_test = list(data_test['Sequence'])
id_test = list(data_test['ID'])

amino_acid_composition_list_train = []
amino_acid_composition_list_test = []

for i in sequence_data_train:
    amino_acid_composition_list_train.append(get_amino_acid_composition(i))

for i in sequence_data_test:
    amino_acid_composition_list_test.append(get_amino_acid_composition(i))

column_names = split('ARNDCEQGHILKMFPSTWYV')
amino_acid_composition_data_train = pd.DataFrame(amino_acid_composition_list_train,columns=column_names)
amino_acid_composition_list_test = pd.DataFrame(amino_acid_composition_list_test,columns=column_names)

train_x = amino_acid_composition_data_train
train_y = data_train['Lable']
val_x = amino_acid_composition_list_test



# model with feature selection using pipeline
anti_fungal_peptide_prediction_model = Pipeline([
  ('feature_selection', SelectFromModel(LinearSVC(penalty="l1", dual=False))),
  ('classification', ExtraTreesClassifier(n_estimators=400))
])

anti_fungal_peptide_prediction_model.fit(train_x,train_y,)
val_y = list(anti_fungal_peptide_prediction_model.predict(val_x))


#Result with test data
result = {'ID':id_test, 'Label':val_y}
result = pd.DataFrame(result, columns=['ID','Label'])

#Generating the output file result.csv
result.to_csv('./result.csv', index=False,header=True)
