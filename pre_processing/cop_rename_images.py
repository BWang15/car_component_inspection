import cv2
import os
from constant import formated_data_dir, deleted_data_dir

if __name__ == '__main__':
    count = 0
    for root, dirs, files in os.walk(deleted_data_dir):
        for f in files:
            if f.find('.jpg') != -1 or f.find('.png') != -1:
                digit_count = 0
                img = cv2.imread(root + '/' + f)
                cv2.imwrite(formated_data_dir + '/' + str(count) + '.jpg', img)
                count = int(count) + 1
