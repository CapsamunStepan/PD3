import random
import os
import shutil
import pandas as pd

extr_new_dir = 'random_created_dataset'
os.makedirs(extr_new_dir, exist_ok=True)

num_list = list(range(1, 10001))
random.shuffle(num_list)

file = 'annotation.csv'
data = pd.read_csv(file)

i = 0
for path in data['Relative Path']:
    new_name = extr_new_dir + '//' + str(num_list[i]) + '.jpg'
    i += 1
    shutil.copy(path, new_name)
