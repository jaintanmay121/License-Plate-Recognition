from skimage.io import imread
from skimage.filters import threshold_otsu
import matplotlib.pyplot as plt

filename = './img.png'

import cv2
car_image = imread(filename, as_gray=True)


fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.imshow(car_image, cmap="gray")
threshold_value = threshold_otsu(car_image)
binary_car_image = car_image > threshold_value
ax2.imshow(binary_car_image, cmap="gray")


from skimage import measure
from skimage.measure import regionprops
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# this gets all the connected regions and groups them together
label_image = measure.label(binary_car_image)


plate_dimensions = (0.03*label_image.shape[0], 0.08*label_image.shape[0], 0.15*label_image.shape[1], 0.3*label_image.shape[1])
plate_dimensions2 = (0.08*label_image.shape[0], 0.25*label_image.shape[0], 0.15*label_image.shape[1], 0.45*label_image.shape[1])
min_height, max_height, min_width, max_width = plate_dimensions
plate_objects_cordinates = []
plate_like_objects = []

fig, (ax1) = plt.subplots(1)
ax1.imshow(car_image, cmap="gray")
flag =0

for region in regionprops(label_image):

    if region.area < 50:
        continue

    min_row, min_col, max_row, max_col = region.bbox

    region_height = max_row - min_row
    region_width = max_col - min_col

    if region_height >= min_height and region_height <= max_height and region_width >= min_width and region_width <= max_width and region_width > region_height:
        flag = 1
        plate_like_objects.append(binary_car_image[min_row:max_row,
                                  min_col:max_col])
        plate_objects_cordinates.append((min_row, min_col,
                                         max_row, max_col))
        rectBorder = patches.Rectangle((min_col, min_row), max_col - min_col, max_row - min_row, edgecolor="red",
                                       linewidth=2, fill=False)
        ax1.add_patch(rectBorder)


if(flag == 1):
    plt.show()

if(flag==0):
    min_height, max_height, min_width, max_width = plate_dimensions2
    plate_objects_cordinates = []
    plate_like_objects = []

    fig, (ax1) = plt.subplots(1)
    ax1.imshow(car_image, cmap="gray")
    for region in regionprops(label_image):
        if region.area < 150:
            continue
        min_row, min_col, max_row, max_col = region.bbox
        rt=max_row-min_row
        rh=max_col-min_col
        #if region_height >= min_height and region_height <= max_height and region_width >= min_width and region_width <= max_width and region_width > region_height:
        if rt >= min_height and rt <= max_height and rh >= min_width and rh <= max_width and rh > 1.3*rt :
            plate_like_objects.append(binary_car_image[min_row:max_row,
                                      min_col:max_col])
            plate_objects_cordinates.append((min_row, min_col,
                                             max_row, max_col))
            rectBorder = patches.Rectangle((min_col, min_row), rh, rt, edgecolor="red",
                                           linewidth=2, fill=False)
            ax1.add_patch(rectBorder)
    plt.show()