import cv2
import os

class VideoToImage:

    # Converts a video to a folder of individual frames
    # Written by Matt Sielecki

    # Source Folder and Source Video
    video_folder = "./Videos" 
    video_name = "video.mp4"

    # Destination Folder of the frames
    save_folder = "./SlicedVideos"

    def video_to_image(video_folder_passed, video_name_passed, save_folder_passed):
        if not(os.path.exists(save_folder_passed)):
            os.mkdir(save_folder_passed)


        directory = video_name_passed[:-4]
        path = os.path.join(save_folder_passed, directory)
        if not(os.path.exists(path)):
            os.mkdir(path)

        vidcap = cv2.VideoCapture(video_folder_passed + "/" + video_name_passed)
        success,image = vidcap.read()
        count = 0
        while success:
            cv2.imwrite(path + "/frame_%d.jpg" % count, image)     # save frame as JPEG file      
            success,image = vidcap.read()
            print('Read a new frame: ', success)
            count += 1

    video_to_image(video_folder, video_name, save_folder)

