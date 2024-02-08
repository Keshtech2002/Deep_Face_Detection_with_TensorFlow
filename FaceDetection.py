import tensorflow as tf
import json # Work with json files for label
import numpy as np
import matplotlib.pyplot as plt
import os
import time
import uuid # allows to create unique filenames automatically uuid.uuid1()
import cv2

def load_image(x): 
    byte_img = tf.io.read_file(x)
    img = tf.io.decode_jpeg(byte_img)
    return img

if __name__=="__main__":
    Main()