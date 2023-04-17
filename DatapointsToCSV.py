import numpy as np
import cv2
import csv

# Write an array to a csv file
# Written by Matt Sielecki

class DatapointsToCSV:

    file_name = 'bestfile.csv'
    
    # Image to read
    image_name = './abImage.jpg'
    data = cv2.imread(image_name, 0)

    # rounds data to 2 decimal places to be more readable
    data_rounded = np.round(data, 2)

    def save_CSV(file_name_passed, data_passed):

        with open(file_name_passed, 'w') as csvfile:
            # creating a csv writer object
            csvwriter = csv.writer(csvfile)
            
            # writing the data rows
            csvwriter.writerows(data_passed)

        print("file saved as: " + file_name_passed)
    
    save_CSV(file_name, data_rounded)

    