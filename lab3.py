import csv
import os

data_directory = 'dataset'
project_directory = os.getcwd()

data_list = []

for root, dirs, files in os.walk(data_directory):
    for file in files:
        relative_path = os.path.join(root, file)
        absolute_path = os.path.join(project_directory, relative_path)
        class_label = os.path.basename(root)
        data_list.append([absolute_path, relative_path, class_label])

annotation_file = "annotation.csv"
with open(annotation_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Absolute Path', 'Relative Path', 'Class Label'])
    writer.writerows(data_list)

print(f"Файл-аннотация {annotation_file} успешно создан.")
