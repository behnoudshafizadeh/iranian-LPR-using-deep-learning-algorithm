import glob, os

# put your own path here

dataset_path = '/home/user1/YoloV3-Custom-Object-Detection-master/training/images'

# Percentage of images to be used for the test set
percentage_test = 30;

# Create and/or truncate train.txt and test.txt
file_train = open('train.txt', 'w')  
file_test = open('test.txt', 'w')

# Populate train.txt and test.txt
counter = 1  
index_test = round(100 / percentage_test)  
for pathAndFilename in glob.iglob(os.path.join(dataset_path, "*.png")):  
    title, ext = os.path.splitext(os.path.basename(pathAndFilename))

    if counter == index_test+1:
        counter = 1
        file_test.write(dataset_path + "/" + title + '.png' + "\n")
    else:
        file_train.write(dataset_path + "/" + title + '.png' + "\n")
        counter = counter + 1
