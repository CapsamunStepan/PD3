import csv
import os


def get_image_paths(dataset_path):
    image_paths = []
    for class_name in os.listdir(dataset_path):
        class_path = os.path.join(dataset_path, class_name)

        # Проверяем, что это директория
        if os.path.isdir(class_path):
            # Проходимся по всем файлам внутри директории класса
            for image_name in os.listdir(class_path):
                image_path = os.path.join(class_path, image_name)

                # Создаем относительный путь относительно проекта
                relative_path = os.path.relpath(image_path, dataset_path)
                relative_path = os.path.join('dataset', relative_path)

                # Добавляем информацию о классе и полный путь к изображению в список
                image_paths.append([image_path, relative_path, class_name])

    return image_paths


def get_classes(dataset_path):
    class_list = []
    for class_name in os.listdir(dataset_path):
        class_list.append(class_name)
    return class_list


def create_af(af_path, d_list):
    with open(af_path, mode='w', newline='') as file_:
        writer = csv.writer(file_)
        writer.writerow(['Absolute Path', 'Relative Path', 'Class Label'])
        writer.writerows(d_list)

    return f"Файл-аннотация {af_path} успешно создан."


if __name__ == "__main__":
    project_path = os.getcwd()
    project_path = os.path.join(project_path, 'dataset')
    print(get_classes(project_path))
    # data_list = get_image_paths(project_path)
    # annotation_file = "annotation.csv"
    # create_af(annotation_file, data_list)
