import numpy as np
import pandas as pd

data = pd.read_csv("./archives/mtsdata/HAART/training.csv")

# print(data.shape)


# --------------------------


exclusions = ['ParticipantNo', ' "Substrate"', ' "Cover"', ' "Gesture"']
cell_columns = [col for col in list(data.columns) if col not in exclusions]
# print(data.columns)
x_train = data.groupby(['ParticipantNo', ' "Substrate"', ' "Cover"', ' "Gesture"'])[cell_columns].apply(lambda x : x.values.tolist()).tolist()
print('X Train Len ', len(x_train))
print('X Train[0] Len ', len(x_train[0]))
print('X Train[0][0] Len ', len(x_train[0][0]))

np.save('./archives/mtsdata/HAART/x_train',x_train, allow_pickle=True)


# --------------------------


y_train = data[['ParticipantNo', ' "Substrate"', ' "Cover"' , ' "Gesture"']]
y_train = y_train.groupby(['ParticipantNo', ' "Substrate"', ' "Cover"', ' "Gesture"'])[' "Gesture"'].apply(lambda x : x.values.tolist()).tolist()

for ind in range(len(y_train)):
    y_train[ind] = y_train[ind][0]
# print(y_train)
print('Y Train ', len(y_train))
np.save('./archives/mtsdata/HAART/y_train',y_train, allow_pickle=True) 

# --------------------------

test_data = pd.read_csv("./archives/mtsdata/HAART/testWITHLABELS.csv")
test_data = test_data.drop('Sequence', axis=1)

exclusions = ['ParticipantID', 'Substrate', 'Cover', 'Gesture']

cell_columns = [col for col in list(test_data.columns) if col not in exclusions]

x_test = test_data.groupby(['ParticipantID', 'Substrate', 'Cover', 'Gesture'])[cell_columns].apply(lambda x : x.values.tolist()).tolist()
print('X Test Len ', len(x_test))
print('X Test[0] Len ', len(x_test[0]))
print('X Test[0][0] Len ', len(x_test[0][0]))
np.save('./archives/mtsdata/HAART/x_test', x_test, allow_pickle=True) 




# --------------------------

y_test = test_data[['ParticipantID', 'Substrate', 'Cover', 'Gesture']]
y_test = test_data.groupby(['ParticipantID', 'Substrate', 'Cover', 'Gesture'])['Gesture'].apply(lambda x : x.values.tolist()).tolist()

for ind in range(len(y_test)):
    y_test[ind] = y_test[ind][0]

print('Y Test ', len(y_test))
np.save('./archives/mtsdata/HAART/y_test', y_test, allow_pickle=True)
