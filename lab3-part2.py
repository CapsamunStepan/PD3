import csv
import os
import shutil

data_directory = 'dataset'
project_directory = os.getcwd()
destination_directory = 'new_dataset'
# create new directory if it does not exist
os.makedirs(destination_directory, exist_ok=True)

new_data_list = []

for root, dirs, files in os.walk(data_directory):
    for file in files:
        relative_path = os.path.join(root, file)

        class_label = os.path.basename(root)

        new_file_name = f'{class_label}_{file}'
        rel_path = os.path.join(destination_directory, new_file_name)
        abs_path = os.path.join(project_directory, rel_path)
        new_data_list.append([abs_path, rel_path, class_label])

        shutil.copy(relative_path, rel_path)


new_annotation_file = 'new_annotation.csv'

with open(new_annotation_file, mode='w', newline='') as annotation_csv:
    annotation_writer = csv.writer(annotation_csv)
    annotation_writer.writerow(['Absolute Path', 'Relative Path', 'Class Label'])
    annotation_writer.writerows(new_data_list)

print(f"Файл-аннотация {new_annotation_file} успешно создан.")