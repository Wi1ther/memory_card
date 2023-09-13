#для начала скопируй сюда интерфейс "Умных заметок" и проверь его работу
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QVBoxLayout,
QPushButton, QLayout, QLineEdit, QTextEdit, QListWidget, QHBoxLayout, QInputDialog)
import json
app = QApplication([])
notes = []
MainWin = QWidget()
MainWin.setWindowTitle('Умные заметки')
MainWin.resize(900,600)
Notetext = QTextEdit()
listLable = QLabel('Список заметок')
NoteList = QListWidget()
buttoncreate = QPushButton('Создать заметку')
buttondelete = QPushButton('Удалить заметку')
buttonsave = QPushButton('Сохранить заметку')
tagLable = QLabel('Список тегов')
taglist = QListWidget()
searchtag = QLineEdit()
searchtag.setPlaceholderText('Введите тег...')
buttonadd = QPushButton('Добавить к заметке')
buttonunplug = QPushButton('Открепить от заметки')
buttonsearch = QPushButton('Искать заметки по тегу')
MainLayout = QHBoxLayout()
leftLayout = QVBoxLayout()
leftLayout.addWidget(Notetext)
rightLayout = QVBoxLayout()
rightLayout.addWidget(listLable)
rightLayout.addWidget(NoteList)
layoutbuttonnote = QHBoxLayout()
layoutbuttonnote.addWidget(buttoncreate)
layoutbuttonnote.addWidget(buttondelete)
rightLayout.addLayout(layoutbuttonnote)
rightLayout.addWidget(buttonsave)
rightLayout.addWidget(tagLable)
rightLayout.addWidget(taglist)
rightLayout.addWidget(searchtag)
layoutbutton = QHBoxLayout()
layoutbutton.addWidget(buttonadd)
layoutbutton.addWidget(buttonunplug)
rightLayout.addLayout(layoutbutton)
rightLayout.addWidget(buttonsearch)
MainLayout.addLayout(leftLayout, stretch = 2)
MainLayout.addLayout(rightLayout, stretch = 1)
MainWin.setLayout(MainLayout)
def show_note():
    key = NoteList.selectedItems()[0].text()
    for note in notes:
        if notes[0] == key:
            Notetext.setText(note[1])
            taglist.clear()
            taglist.addItems(note[2])
NoteList.itemClicked.connect(show_note)
NoteList.addItems(notes)
MainWin.show()
fileNumber = 0
note = []
while True:
    fileName = str(fileNumber) + '.txt'
    try:
        with open(fileName,'r',encoding = 'utf-8') as file:
            for line in file:
                line = line.replace('\n','')
                note.append(line)
        tags = note[2].split(' ')
        note[2] = tags
        notes.append(note)
        note = []
        fileNumber += 1
    except IOError:
        break
    for note in notes:
        NoteList.addItem(note[0])
app.exec_()
#затем запрограммируй демо-версию функционала
