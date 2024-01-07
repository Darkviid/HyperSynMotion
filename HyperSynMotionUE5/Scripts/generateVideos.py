#Generate a video from a set of images on each subfolder of a given folder

import os
import sys
import cv2
import numpy as np
import glob
import argparse
import shutil
import subprocess
import time
from tqdm import tqdm

# The parent directory of this file location + /Screenshots
dir_path = os.path.dirname(os.path.realpath(__file__)) + "/../Screenshots"
dir_path = os.path.normpath(dir_path)
print("Looking for images in dir_path: " + dir_path)

animationFolders = ['animation_w_0', 'animation_m_0']

def generateVideoFromImages(folder, outputFolder, fps, width, height, extension):
    #print("Generating video from images in folder: " + folder)
    #print("Output folder: " + outputFolder)
 
    if not os.path.exists(outputFolder):
        os.makedirs(outputFolder)

    for subfolder in os.listdir(folder):
        subfolderPath = os.path.join(folder, subfolder)
        if os.path.isdir(subfolderPath):
            print("Exploring subfolder: " + subfolder)
            #Check if there are more subfolders inside
            generateVideoFromImages(subfolderPath, subfolderPath, fps, width, height, extension)
            
            images = glob.glob(subfolderPath + "/*." + extension)
            images.sort()
            if len(images) > 0:
                print("Generating video from images in folder: " + subfolderPath)
                print("Number of images: " + str(len(images)))
                videoName = os.path.join(outputFolder, subfolder + ".mp4")
                print("Video name: " + videoName)
                fourcc = cv2.VideoWriter_fourcc(*'mp4v')
                video = cv2.VideoWriter(videoName, fourcc, fps, (width, height))
                for image in tqdm(images):
                    #print("Adding image: " + image)
                    img = cv2.imread(image)
                    video.write(img)
                video.release()
                print("Video generated: " + videoName)
            else:
                print("No images found in folder: " + subfolderPath)
        else:
            #print("Not a folder: " + subfolderPath)
            pass
            




fps = 30
width = 1920
height = 1080
extension = "png"


print("FPS: " + str(fps))
print("Width: " + str(width))
print("Height: " + str(height))
print("Extension: " + extension)
    
generateVideoFromImages(dir_path, dir_path, fps, width, height, extension)


#for each animation folder
#for animationFolder in animationFolders:
#    generateVideoFromImages(dir_path + "/" + animationFolder, dir_path + "/" + animationFolder + "/videos", 30, 1920, 1080, "png")