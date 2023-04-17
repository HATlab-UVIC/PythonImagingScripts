import open3d as o3d
import numpy as np
import sys

# Reads a ply and prints its points 
# Written by Matt Sielecki

class ReadingPLY:

    # Name of the file
    file_name = './noName.ply'

    def read_PLY(file_name_passed):
        plydata = o3d.io.read_point_cloud(file_name_passed)

        np.set_printoptions(threshold=sys.maxsize)
        print(np.asarray(plydata.points))

    read_PLY(file_name)


