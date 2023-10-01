from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton, QPushButton, QLabel, QButtonGroup)
from random import *


app=QApplication([])
screen=QWidget()

h=randint(1,3)

screen.resize(300,300)

res=QLabel(' ')


button1=QPushButton('Камень')

button2=QPushButton('Ножницы')

button3=QPushButton('Бумага')

line1=QVBoxLayout()

line1.addWidget(res)
line1.addWidget(button1)
line1.addWidget(button2)
line1.addWidget(button3)

screen.setLayout(line1)

def olt1():
    if h==1:
        text='Ничья, робот выбрал камень'
    elif h ==2:
        text='Проигрыш, робот выбрал бумагу'
    else:
        text='Победа, робот выбрал ножницы'
    res.setText(str(text))
    button1.hide()
    button2.hide()
    button3.hide()
    

def olt2():
    if h==1:
        text='Проигрыш, робот выбрал камень'
    elif h ==2:
        text='Победа, робот выбрал бумагу'
    else:
        text='Ничья, робот выбрал ножницы'
    res.setText(str(text))
    button1.hide()
    button2.hide()
    button3.hide()
    
def olt3():
    if h==1:
        text='Победа, робот выбрал камень'
    elif h ==2:
        text='Ничья, робот выбрал бумагу'
    else:
        text='Проигрыш, робот выбрал ножницы'
    res.setText(str(text))
    button1.hide()
    button2.hide()
    button3.hide()
    

button1.clicked.connect(olt1)
button2.clicked.connect(olt2)
button3.clicked.connect(olt3)



    

screen.show()
app.exec()