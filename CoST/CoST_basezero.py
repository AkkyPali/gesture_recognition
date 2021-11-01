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
# # train_data = train_data[:10]

test = data['subject'] > 21
test_data= data[test]
# test_data = test_data[:10]

# # # ---- STEP 4 ------ reshape X_train data into 3D data ------

# TRAIN DATA
exclusions = ['subject', ' variant', ' gesture', 'iteration']
cell_columns = [col for col in list(train_data.columns) if col not in exclusions]
x_train_data_3d = train_data.groupby(['subject', ' variant', ' gesture', 'iteration'])[cell_columns].apply(lambda x : x.values.tolist()).tolist()

x_train_data_3d = pd.DataFrame(x_train_data_3d) 
fig, ax = plt.subplots(1) # Creates figure fig and add an axes, ax.
fig2, ax2 = plt.subplots(1) # Another figure
# for video_index in x_train_data_3d:

# for frame_index in x_train_data_3d[0]: 
ch_1 = []
for frame_index in range(len(x_train_data_3d[0])): 
    ch_1.append(x_train_data_3d[0][frame_index][0])
ax.plot(ch_1) # Channels in first frame 

cell_columns = [col for col in list(train_data.columns) if col not in exclusions]
train_data.groupby(['subject', ' variant', ' gesture', 'iteration'])[' gesture'].apply(lambda x : x.values.tolist()).tolist()
y_train_data_3d = train_data.groupby(['subject', ' variant', ' gesture', 'iteration'])[' gesture'].apply(lambda x : x.values.tolist()[0]).tolist()

# # TEST DATA
cell_columns = [col for col in list(test_data.columns) if col not in exclusions]
x_test_data_3d = test_data.groupby(['subject', ' variant', ' gesture', 'iteration'])[cell_columns].apply(lambda x : x.values.tolist()).tolist()

cell_columns = [col for col in list(test_data.columns) if col not in exclusions]
y_test_data_3d = test_data.groupby(['subject', ' variant', ' gesture', 'iteration'])[' gesture'].apply(lambda x : x.values.tolist()[0]).tolist()
# print('y test data length is',len(y_train_data_3d), len(y_train_data_3d[0]))

# # # ---- STEP 5 ------ add baseline to make equal lengths ------
zero_frame = []
for i in range(0,64):
   zero_frame.append(0)

# print('Total Number of samples ',len(x_train_data_3d))
# print('Total Number of frames in first sample ',len(x_train_data_3d[6]))
# print('Total Number of channels in F1 for S1 ',len(x_train_data_3d[0][0]))
# print('Ch1 in F1 for S1 ',x_train_data_3d[0][0][0])

#TRAIN DATA
for video_index in range(len(x_train_data_3d)):
    for _ in range(max_len - len(x_train_data_3d[video_index])):
        x_train_data_3d[video_index].append(zero_frame)
    # print(len(x_train_data_3d[video_index]))

ch_1_ = []
for frame_index in range(len(x_train_data_3d[0])): 
    ch_1_.append(x_train_data_3d[0][frame_index][0])
ax2.plot(ch_1_) # Channels in first frame 

# np.save('./archives/mtsdata/CoST/x_train.npy', x_train_data_3d, allow_pickle=True)
# np.save('./archives/mtsdata/CoST/y_train.npy',y_train_data_3d, allow_pickle=True)

# # #TEST DATA
# for video_index in range(len(x_test_data_3d)):
#     for _ in range(max_len - len(x_test_data_3d[video_index])):
#         x_test_data_3d[video_index].append(zero_frame)
    # print(len(x_test_data_3d[video_index]))
# np.save('./archives/mtsdata/CoST/x_test.npy', x_test_data_3d, allow_pickle=True)
# np.save('./archives/mtsdata/CoST/y_test.npy',y_test_data_3d, allow_pickle=True)
