import numpy as np
from PIL import Image
from matplotlib import pyplot as plt
import math
import cv2
import time

MAX_WIDTH = 158 #* 4 
MAX_HEIGHT = 42 #* 3 + 6

def get_screen(grid):
    grid = [[to_ascii(e) for e in row] for row in grid]
    screen = "\n".join(["".join(l) for l in grid])
    return screen

def to_ascii(val):
    if val < 0 or val > 1:
        raise ValueError("val must be between 0 and 1")
    ramp =  "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "[::-1]
    value = math.floor(len(ramp) * val)
    return ramp[value]

def main():
    print_vid("ressources/vid.mp4")
    #print_pic("ressources/arch.jpg")

def print_vid(path):
    vid = extract_video(path)
    for frame in vid[55 * 24::2]:
        grid3 = grayscale(frame)
        grid4 = shrink(grid3)
        print(get_screen(grid4))
        time.sleep(0.03)

def print_pic(path):
    pic = extract_picture(path)
    grid3 = grayscale(pic)
    grid4 = shrink(grid3)
    print(get_screen(grid4))

def extract_picture(path):
   image = Image.open(path) 
   image = np.asarray(image)
   return image

def extract_video(path):
    frames = []
    video = cv2.VideoCapture(path)
    while True:
        read, frame= video.read()
        if not read:
            break
        frames.append(frame)
    frames = np.array(frames)
    print(frames)
    return frames

def grayscale(image):
    return np.mean(image, axis=2) / 256

def shrink(image):
    w = image.shape[1] // MAX_WIDTH
    h = image.shape[0] // MAX_HEIGHT
    new_image = np.zeros((MAX_HEIGHT, MAX_WIDTH))
    for i in range(MAX_HEIGHT):
        for j in range(MAX_WIDTH):
            new_image[i, j] = np.mean(image[i * h: h * (i + 1), j * w: w * (j+1)])


    return new_image


main()
