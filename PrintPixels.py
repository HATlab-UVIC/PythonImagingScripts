import cv2

# Gets all pixels from an image
# Written by Matt Sielecki

class PrintPixels:

    # file name of the image
    file_name = './TestImg.jpg'
    text_name = "./TestImg.txt"

    def pixels_from_image(file_name_passed, text_name_passed):
        img = cv2.imread(file_name_passed, 0)
        rows,cols = img.shape
        with open(text_name_passed, 'w') as file:
            for i in range(rows):
                for j in range(cols):
                    k = img[i,j]
                    file.write("[ row: " + str(i) + ", col: " + str(j) + " ] : "+ str(k) + "\n")
        
        print("file saved as: " + text_name_passed)


    pixels_from_image(file_name, text_name)