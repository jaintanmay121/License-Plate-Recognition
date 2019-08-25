# License Plate Recognition

## Training model for Character Recognition
(trainedModel.sav)

Using the Cross Validation and Support Vector Classification, train the model and save it using pickle.
You can use the pretrained model or train yourself uing the file TrainCharacters.py and extracting the dataset from training_images.rar.

## Detect the Plate
(DetectPlate.py)
1. Read the Image
2. Convert the car image into Grayscale.
3. The image is then inverted so that the characters are easy to read by the machine.
4. Considering the min and max height and width of a standard license plate.
5. Checking different regions of the image for the considered height and width values to finally locate the number plate.


## Searching and Predicting Characters in the License Plate
(PredictCharacters.py)

Considering the min and max dimensions for the characters in the license plate, we locate the characters similarly. Using the pretrained character recgnition model, we predict the characters.

## Using the repo

To run the code, add the path of image into the DetectPlate.py file.
Then just run the PredictCharacters.py.
