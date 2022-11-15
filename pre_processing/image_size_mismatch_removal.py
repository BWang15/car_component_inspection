import os
import cv2

root_dir = r'D:/naolu/car_component_inspection/data/data_original'

if __name__ == '__main__':
    for root, dirs, files in os.walk(root_dir):
        for f in files:
            if f.find('.jpg') != -1 or f.find('.png') != -1:
                img = cv2.imread(root + '/' + f)
                height, width, channels = img.shape
                print(height, width, channels)
