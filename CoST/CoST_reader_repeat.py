import numpy as np
from numpy.core.numeric import False_
import pandas as pd
from pandas.core.series import Series
import matplotlib.pyplot as plt 
from matplotlib import pyplot 
import itertools
# STEP1 in cost_reader.py ------------

# ---- STEP 2 ------ Filter out variant 3 from data ------
data = pd.read_csv("./archives/mtsdata/CoST/data_with_iteration.csv")
data_var3 = data[' variant'] != 3
data = data[data_var3]

max_len = max(data[' frame'])
print('Max length is', max_len)
data = data.drop(' frame', axis = 1)

# # ---- STEP 3.a ------ divide train and test data ------

# #create training data
train = data['subject'] <= 21
train_data = data[train]
# train_data = train_data[:10]

test = data['subject'] > 21
test_data= data[test]
# test_data = test_data[:10]

# # # ---- STEP 4 ------ reshape X_train data into 3D data ------

# TRAIN DATA
exclusions = ['subject', ' variant', ' gesture', 'iteration']
cell_columns = [col for col in list(train_data.columns) if col not in exclusions]
x_train_data_3d = train_data.groupby(['subject', ' variant', ' gesture', 'iteration'])[cell_columns].apply(lambda x : x.values.tolist()).tolist()

cell_columns = [col for col in list(train_data.columns) if col not in exclusions]
train_data.groupby(['subject', ' variant', ' gesture', 'iteration'])[' gesture'].apply(lambda x : x.values.tolist()).tolist()
y_train_data_3d = train_data.groupby(['subject', ' variant', ' gesture', 'iteration'])[' gesture'].apply(lambda x : x.values.tolist()[0]).tolist()

# # TEST DATA
cell_columns = [col for col in list(test_data.columns) if col not in exclusions]
x_test_data_3d = test_data.groupby(['subject', ' variant', ' gesture', 'iteration'])[cell_columns].apply(lambda x : x.values.tolist()).tolist()

cell_columns = [col for col in list(test_data.columns) if col not in exclusions]
y_test_data_3d = test_data.groupby(['subject', ' variant', ' gesture', 'iteration'])[' gesture'].apply(lambda x : x.values.tolist()[0]).tolist()
# print('y test data length is',len(y_train_data_3d), len(y_train_data_3d[0]))

# ## STEP 6 --- repeat list values until length is (1747)
for video_index in range(len(x_train_data_3d)):
    # print('Before length',len(x_train_data_3d[video_index]))  
    for frame_index in range(len(x_train_data_3d[video_index])):
        for x in itertools.cycle(x_train_data_3d[video_index]):
            curr_len = len(x_train_data_3d[video_index])
            if curr_len >= max_len:
                break
            x_train_data_3d[video_index].append(x_train_data_3d[video_index][frame_index])
    # print('After length',len(x_train_data_3d[video_index]))
np.save('./archives/mtsdata_ucr/CoST/x_train.npy', x_train_data_3d, allow_pickle=True)
np.save('./archives/mtsdata/CoST/y_train.npy',y_train_data_3d, allow_pickle=True)

# # #TEST DATA
for video_index in range(len(x_test_data_3d)):
    print('Before length',len(x_test_data_3d[video_index])) 
    for frame_index in range(len(x_test_data_3d[video_index])): 
        for x in itertools.cycle(x_test_data_3d[video_index]):
            curr_len = len(x_test_data_3d[video_index])
            if curr_len >= max_len:
                break
            x_test_data_3d[video_index].append(x_test_data_3d[video_index][frame_index])
    # print('After length',len(x_test_data_3d[video_index]))
np.save('./archives/mtsdata/CoST/x_test.npy', x_test_data_3d, allow_pickle=True)
np.save('./archives/mtsdata/CoST/y_test.npy',y_test_data_3d, allow_pickle=True)
