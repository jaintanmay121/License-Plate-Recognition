import os
import numpy as np
from sklearn.svm import SVC
from skimage.io import imread
from skimage.filters import threshold_otsu

letters = [
            '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D',
            'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T',
            'U', 'V', 'W', 'X', 'Y', 'Z'
        ]

def read_training_data(training_directory):
    image_data = []
    target_data = []
    for each_letter in letters:
        for each in range(10):
            image_path = os.path.join(training_directory, each_letter, each_letter + '_' + str(each) + '.jpg')
            # read each image of each character
            img_details = imread(image_path, as_gray=True)
            binary_image = img_details < threshold_otsu(img_details)
            flat_bin_image = binary_image.reshape(-1)
            image_data.append(flat_bin_image)
            target_data.append(each_letter)

    return (np.array(image_data), np.array(target_data))


print('reading data')
training_dataset_dir = './training_images'
image_data, target_data = read_training_data(training_dataset_dir)
print('reading data completed')

svc_model = SVC(kernel='linear', probability=True)


print('training model')

svc_model.fit(image_data, target_data)


import pickle
print("model trained.saving model..")
filename = './trainedModel.sav'
pickle.dump(svc_model, open(filename, 'wb'))
print("model saved")