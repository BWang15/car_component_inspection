import os

root_dir = r'D:\naolu\car_component_inspection\data\data_original'

if __name__ == '__main__':
    for root, dirs, files in os.walk(root_dir):
        for f in files:
            if f.find('.json') != -1:
                os.remove(root + '/' + f)