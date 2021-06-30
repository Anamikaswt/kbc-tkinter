from cProfile import label
from cgitb import text
import imghdr
from tkinter import font
from tkinter.font import BOLD, ITALIC
from tkinter import Tk,  Frame, Label, Button 
from time import sleep

from click import command

class Question:
    def __init__(self, question, answers, correctLetter):
        self.question = question
        self.answers = answers
        self.correctLetter = correctLetter


    def check(self, letter, view):
        global right
        if(letter == self.correctLetter):
            label = Label(view, font=("Arial",20,BOLD),text="Right!")
            right += 1
        else:
            label = Label(view,font=("Arial",20,BOLD), text="Wrong!")
        label.pack()
        view.after(1000, lambda *args: self.unpackView(view))


    def getView(self, window):
        view = Frame(window)
        Label(view, font=("Arial",20,BOLD),text=self.question).pack()
        Button(view, font=("Arial",15,BOLD),bd=10,height=2,width=15, text=self.answers[0],fg="blue", bg="grey", command=lambda *args: self.check("A", view)).pack()
        Button(view, font=("Arial",15,BOLD),bd=10,height=2,width=15,text=self.answers[1],fg="blue", bg="grey", command=lambda *args: self.check("B", view)).pack()
        Button(view, font=("Arial",15,BOLD),bd=10,height=2,width=15,text=self.answers[2],fg="blue", bg="grey", command=lambda *args: self.check("C", view)).pack()
        Button(view, font=("Arial",15,BOLD),bd=10,height=2,width=15,text=self.answers[3], fg="blue", bg="grey",command=lambda *args: self.check("D", view)).pack()
        return view

    def unpackView(self, view):
        view.pack_forget()
        askQuestion()

def askQuestion():
    global questions, window, index, button, right, number_of_questions 
    if(len(questions) == index + 1):
        Label(window, font=("Arial",20,BOLD),text="Thank you for answering the questions. " + str(right) + " of " + str(number_of_questions) + " questions answered right").pack()
        Button(window,font=("Arial",15,BOLD),bd=10,height=2,width=15,text="Click me for Exit",bg="grey",command=window.destroy).pack()
        return
    button.pack_forget()
    index += 1
    questions[index].getView(window).pack()

questions = []
file = open("questions.txt", "r")
line = file.readline()
while(line != ""):
    questionString = line
    answers = []
    for i in range (4):
        answers.append(file.readline())

    correctLetter = file.readline()
    correctLetter = correctLetter[:-1]
    questions.append(Question(questionString, answers, correctLetter))
    line = file.readline()
file.close()
index = -1
right = 0
number_of_questions = len(questions)

window = Tk()
label=Label(window,font=("Arial",30,BOLD),text= " $$$$$ WELCOME IN KBC GAME $$$$$ CREATED BY ANAMIKA SINGH").pack()

from tkinter import *
from random import randint
window.geometry('500x300')
# ws.title('welcome to kbc')
img= PhotoImage(file="/home/anamika/Desktop/anamika.png")
image_list=[img]
pick_number=randint(0,0)
image_lable=Label(image=image_list[pick_number])
image_lable.pack(pady=20)
button = Button(window, font=("Arial",20,BOLD),bd=10,height=2,width=6,text="Start", command=askQuestion)
button.pack()

window.mainloop()