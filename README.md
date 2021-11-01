Gesture Recognition – ReadMe.md

This project focuses on running latest Neural Network and ensemble model on time series gesture recognition datatsets. There are two datasets used in this project. 
1.	Human-Animal Affective Robot Touch (HAART) : This dataset has equal time duration for each sample
-	Gestures: no touch, constant, rub, pat, scratch, stroke & tickle
-	Original Training Dataset = 578*432 Rows
-	Original Test Dataset = 251*432 Rows
2.	Corpus of Social Touch (CoST): This dataset has varied time duration sample length
-	3 variants (normal/gentle/rough) * 6 times * 14 Gestures * 31 Participants 
-	Duration - 75ms to 9.6 sec sampled at 135Hz
-	Gestures: Grab, hit, massage, pat, pinch, poke, press, rub, scratch, slap, squeeze, stroke, tap, and tickle
Challenge:
To be able to feed the data to neural network models, they have to be of equal length, however due to CoST’s varied length it had to be processed. For this there were multiple approaches as listed below: 
1.	Linearly Interpolate the time series of each dimension for every given MTS, thus each time series will have a length equal to the longest time series’ length. This form of pre-processing has also been used by Ratanamahatana and Keogh (2005) to show that the length of a time series is not an issue for TSC problems

2.	Fill the difference in frames of short samples to match the longest sample timeframe count

Approach 1: Linearly Interpolate CoST data : 
- Step 1: Adding new column iterations to the data : Each gesture performed by the subject was recorded 6 times. Necessary to get the max length for interpolation
- Step 2: Calculate max length, drop values (variant 3(missing data), frame)
- Step 3: Divide training data (21 subjects) vs test data (10 subjects).
- Step 4: Reshape the training and test data into 3D data grouped by ['subject', ' variant', ' gesture', 'iteration']
- Step 5: Resample and interpolate x_train and x_test data to get equal length samples using resample() and interpolate(). Convert interpolated data into .npy files

Approach 2: Add base 0 values to CoST data
- Step 1: Adding new column iterations to the data : Each gesture performed by the subject was recorded 6 times. Necessary to get the max length for interpolation
- Step 2: Calculate max length, drop values (variant 3(missing data), frame)
- Step 3: Divide training data (21 subjects) vs test data (10 subjects).
- Step 4: Reshape the training and test data into 3D data grouped by ['subject', ' variant', ' gesture', 'iteration']
- Step 5: Calculate the longest length and take the difference between the longest and shortest frame. The insert the zeroes to match the difference towards the end of the sample get equal length samples using resample() and interpolate(). Convert processed data into .npy files

Results: 
Linearly Interpolated: 7% accuracy
Base zero: 31% accuracy
