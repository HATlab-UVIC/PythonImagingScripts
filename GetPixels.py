import cv2

# Gets all pixels from an image
# Written by Matt Sielecki

class GetPixels:

    # file name of the image
    file_name = './abImage.jpg'

    def pixels_from_image(file_name_passed):
        img = cv2.imread(file_name_passed, 0)
        rows, cols = img.shape

        for i in range(rows):
            for j in range(cols):
                k = img[i,j]
                print(k, end=', ')
            print()


    pixels_from_image(file_name)