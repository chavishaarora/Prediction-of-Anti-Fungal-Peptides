import pandas as pd
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.feature_selection import SelectFromModel
from sklearn.pipeline import Pipeline
from sklearn.svm import LinearSVC
from sklearn.model_selection import train_test_split



def split(word):
    return [char for char in word]

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




file_path_train = 'C:/Users/sarth/OneDrive/Desktop/iqb2020/train.csv'
file_path_test = 'C:/Users/sarth/OneDrive/Desktop/iqb2020/test.csv'



data_train = pd.read_csv(file_path_train, delimiter=',')
data_test = pd.read_csv(file_path_test, delimiter=',')
sequence_data_train = list(data_train['Sequence'])
sequence_data_test = list(data_test['Sequence'])
id_test = list(data_test['ID'])

amino_acid_composition_list_train = []


for i in sequence_data_train:
    amino_acid_composition_list_train.append(get_amino_acid_composition(i))


column_names = split('ARNDCEQGHILKMFPSTWYV')
amino_acid_composition_data_train = pd.DataFrame(amino_acid_composition_list_train,columns=column_names)

train_x = amino_acid_composition_data_train
train_y = data_train['Lable']

X_train, X_test, y_train, y_test = train_test_split(train_x, train_y, test_size=0.3,random_state=1)


anti_fungal_peptide_prediction_model = Pipeline([
  ('feature_selection', SelectFromModel(LinearSVC(penalty='l1',dual=False))),
  ('classification', ExtraTreesClassifier(n_estimators=400))
])


anti_fungal_peptide_prediction_model.fit(X_train,y_train)

print(anti_fungal_peptide_prediction_model.score(X_test,y_test))


