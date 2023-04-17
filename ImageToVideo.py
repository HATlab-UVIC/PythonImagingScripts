import cv2
import os

# Converts a batch of images into a video
# Written by Matt Sielecki

class ImageToVideo:

    # Name of the video you will create
    video_name = ""

    # Source and Destination folder
    image_folder = "./Video"

    def ConvertImageToVideo(video_name_passed, image_folder_passed):

        images = [img for img in os.listdir(image_folder_passed) if img.endswith(".png")]
        frame = cv2.imread(os.path.join(image_folder_passed, images[0]))
        height, width, layers = frame.shape

        video = cv2.VideoWriter(image_folder_passed + video_name_passed, 0, 1, (width,height))

        for image in images:
            video.write(cv2.imread(os.path.join(image_folder_passed, image)))

        cv2.destroyAllWindows()
        video.release()

    ConvertImageToVideo(video_name, image_folder)