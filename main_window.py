import sys
import PyQt5.QtWidgets as qw
import PyQt5.QtGui as qg
from lab3 import create_af, get_image_paths, get_classes

app = qw.QApplication(sys.argv)

window = qw.QMainWindow()
window.setFixedSize(1024, 880)
window.setWindowTitle('Photo App')
icon = qg.QIcon('fav.png')
window.setWindowIcon(icon)
font = qg.QFont()
font.setFamily('Lucida Sans')
font.setPointSize(10)

dataset_path = ''
annotation_path = ''
img_path_list = []

pathLabel = qw.QTextEdit(window)
pathLabel.setReadOnly(True)
pathLabel.setText('')  # Пустой текст по умолчанию
pathLabel.setFont(font)
pathLabel.setGeometry(180, 10, 770, 30)
index = None
label = qw.QLabel(window)
label.setGeometry(300, 150, 500, 500)
nextCat = None
nextDog = None


def create_show_buttons():
    global index
    showCat = qw.QPushButton('cat', window)
    showCat.setGeometry(300, 70, 100, 30)
    showCat.setFont(font)
    showCat.clicked.connect(show_class1)
    showCat.show()

    showDog = qw.QPushButton('dog', window)
    showDog.setGeometry(600, 70, 100, 30)
    showDog.setFont(font)
    showDog.clicked.connect(show_class2)
    showDog.show()


def get_path():
    global dataset_path
    global img_path_list
    dataset_path = qw.QFileDialog.getExistingDirectory(window)
    create_show_buttons()
    img_path_list = get_image_paths(dataset_path)
    pathLabel.setPlainText(dataset_path)


def create_annotation_file():
    global dataset_path
    global annotation_path
    annotation_path = qw.QFileDialog.getExistingDirectory(window)
    annotation_path += '/annotation.csv'
    text = create_af(annotation_path, get_image_paths(dataset_path))
    msg_box = qw.QMessageBox()
    msg_box.setIcon(qw.QMessageBox.Information)
    msg_box.setWindowTitle("Успех")
    msg_box.setText(text)
    msg_box.exec_()


def show_class1():
    global index
    global img_path_list
    global label
    global nextCat
    global nextDog
    index = 0
    img_path = img_path_list[index][0]
    pixmap = qg.QPixmap(img_path)
    label.setPixmap(pixmap)
    label.show()
    try:
        nextDog.destroy()
    except:
        pass
    nextCat = qw.QPushButton('NEXT CAT', window)
    nextCat.setGeometry(300, 120, 100, 30)
    nextCat.setFont(font)
    nextCat.clicked.connect(iterator_cat)
    nextCat.show()


def show_class2():
    global index
    global img_path_list
    global label
    global nextCat
    global nextDog
    index = len(img_path_list) // 2
    img_path = img_path_list[50][0]
    pixmap = qg.QPixmap(img_path)
    label.setPixmap(pixmap)
    label.show()
    try:
        nextCat.destroy()
    except:
        pass
    nextDog = qw.QPushButton('NEXT DOG', window)
    nextDog.setGeometry(600, 120, 100, 30)
    nextDog.setFont(font)
    nextDog.clicked.connect(iterator_dog)
    nextDog.show()


def iterator_cat():
    global index
    global label
    global nextDog
    try:
        nextDog.destroy()
    except:
        pass
    label.destroy()
    if index < len(img_path_list) // 2 - 1:
        index += 1
        img_path = img_path_list[index][0]
        pixmap = qg.QPixmap(img_path)
        label.setPixmap(pixmap)
        label.show()
    else:
        return


def iterator_dog():
    global index
    global label
    global nextCat
    try:
        nextCat.destroy()
    except:
        pass
    label.destroy()
    if index < len(img_path_list):
        index += 1
        img_path = img_path_list[index][0]
        pixmap = qg.QPixmap(img_path)
        label.setPixmap(pixmap)
        label.show()
    else:
        return


openButton = qw.QPushButton('Open catalog', window)
openButton.setGeometry(10, 10, 150, 30)
openButton.setFont(font)
openButton.clicked.connect(get_path)

createAnnotationFile = qw.QPushButton('Create annotation.csv', window)
createAnnotationFile.setGeometry(412, 800, 200, 30)
createAnnotationFile.setFont(font)
createAnnotationFile.clicked.connect(create_annotation_file)

window.show()
sys.exit(app.exec_())
