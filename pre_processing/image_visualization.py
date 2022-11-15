import matplotlib.pyplot as plt
import cv2
import json
from matplotlib.patches import Rectangle
from constant import mask_map, colour_map, img_scale_factor


def plot_polygon(img, json_obj):
    labels = json_obj['shapes']
    img = cv2.resize(img, [256, 144])
    plt.imshow(img)
    for obj in labels:
        points = obj['points']
        if points[0][0] < points[1][0]:
            plt.gca().add_patch((Rectangle((points[0][0], points[0][1]),
                                           abs(points[0][0] - points[1][0]),
                                           abs(points[0][1] - points[1][1]),
                                           facecolor=colour_map[obj['label']],
                                           edgecolor=colour_map[obj['label']], lw=2, alpha=0.2)))
        else:
            plt.gca().add_patch((Rectangle((points[1][0], points[1][1]),
                                           abs(points[0][0] - points[1][0]),
                                           abs(points[0][1] - points[1][1]),
                                           facecolor=colour_map[obj['label']],
                                           edgecolor=colour_map[obj['label']], lw=2, alpha=0.2)))
    # plt.axis(False)
    plt.show()


def plot_resize_img_with_polygon(img, json_obj):
    labels = json_obj['shapes']
    height, width, channels = img.shape
    img = cv2.resize(img, [int(width / img_scale_factor), int(height / img_scale_factor)])
    plt.imshow(img)
    for obj in labels:
        points = obj['points']
        if points[0][0] < points[1][0]:
            plt.gca().add_patch((Rectangle((points[0][0] / img_scale_factor, points[0][1] / img_scale_factor),
                                           abs(points[0][0] - points[1][0]) / img_scale_factor,
                                           abs(points[0][1] - points[1][1]) / img_scale_factor,
                                           facecolor=colour_map[obj['label']],
                                           edgecolor=colour_map[obj['label']], lw=2, alpha=0.2)))
        else:
            plt.gca().add_patch((Rectangle((points[1][0] / img_scale_factor, points[1][1] / img_scale_factor),
                                           abs(points[0][0] - points[1][0]) / img_scale_factor,
                                           abs(points[0][1] - points[1][1]) / img_scale_factor,
                                           facecolor=colour_map[obj['label']],
                                           edgecolor=colour_map[obj['label']], lw=2, alpha=0.2)))
    # plt.axis(False)
    plt.show()


if __name__ == '__main__':
    label = json.load(open(r'D:\naolu\car_component_inspection\data\label\0.json'))
    img = cv2.imread(r'D:\naolu\car_component_inspection\data\data_formated\0.jpg')
    plot_resize_img_with_polygon(img, label)
