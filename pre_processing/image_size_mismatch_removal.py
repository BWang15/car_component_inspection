import os
import cv2

root_dir = r'D:\naolu\car_component_inspection\data\data_formated'

if __name__ == '__main__':
    count = 0
    for root, dirs, files in os.walk(root_dir):
        for f in files:
            if f.find('.jpg') != -1 or f.find('.png') != -1:
                img = cv2.imread(root + '/' + f)
                height, width, channels = img.shape
                if width < height:
                    image = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
                    os.remove(root + '/' + f)
                    cv2.imwrite(root + '/' + f, image)