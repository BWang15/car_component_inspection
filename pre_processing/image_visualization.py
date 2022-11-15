import matplotlib.pyplot as plt
import cv2
import json
from matplotlib.patches import Rectangle


def plot_polygon(img, json_obj):
    mask_map = {'wheel': 1, 'battery': 2, 'engine': 3, 'bumper': 4}
    colour_map = {'wheel': 'green', 'battery': 'red', 'engine': 'blue', 'bumper': 'yellow'}
    labels = json_obj['shapes']
    plt.imshow(img)
    for obj in labels:
        name = mask_map[obj['label']]
        points = obj['points']
        print(name, points)
        if points[0][0] < points[1][0]:
            plt.gca().add_patch((Rectangle((points[0][0], points[0][1]),
                                           abs(points[0][0] - points[1][0]),
                                           abs(points[0][1] - points[1][1]), facecolor=colour_map[obj['label']], edgecolor=colour_map[obj['label']], lw=2, alpha=0.2)))
        else:
            plt.gca().add_patch((Rectangle((points[1][0], points[1][1]),
                                           abs(points[0][0] - points[1][0]),
                                           abs(points[0][1] - points[1][1]), facecolor=colour_map[obj['label']], edgecolor=colour_map[obj['label']], lw=2, alpha=0.2)))
    plt.show()


if __name__ == '__main__':
    label = json.load(open(r'D:\naolu\car_component_inspection\data\label\0.json'))
    img = cv2.imread(r'D:\naolu\car_component_inspection\data\data_formated\0.jpg')
    plot_polygon(img, label)
