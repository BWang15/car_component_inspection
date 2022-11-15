import os
from constant import original_data_dir

if __name__ == '__main__':
    for root, dirs, files in os.walk(original_data_dir):
        for f in files:
            if f.find('.json') != -1:
                os.remove(root + '/' + f)