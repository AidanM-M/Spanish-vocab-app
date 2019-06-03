import tkinter
import random
from tkinter import Tk, Label, Button, Entry, StringVar, DISABLED, NORMAL, END, W, E
import pandas as pd
import random

#Convert datframe to dictionary

df = pd.read_csv("Netflix subtitles/Nuestro Planeta word with translation.csv")

WordDict = {}

for x in range (0, len(df['Spanish'])):
    WordDict.update({df.loc[x, 'Spanish']: df.loc[x, 'English']})
    
    

class SpanishFlashcards:
    def __init__(self, master):
        self.master = master #Master is for the toolbar I think
        master.title("Practise Spanish")
        
        vcmd = master.register(self.validate)
        self.answer = None
        self.correctness = ""
        self.entry = Entry(master, validate="key", validatecommand=(vcmd, '%P'))
        
        self.message = (random.choice(list(WordDict.keys())).strip()).lower()
        self.correct_answer = WordDict.get(self.message).strip()
        
        #The labels and names
        
        #Label(master).grid(row=0)
        #Label(master).grid(row=1)
        
        self.answer_button = Button(master, text="Check", command=self.give_answer)
        
        self.label_text = StringVar()
        self.label_text.set(self.message)
        self.label = Label(master, textvariable=self.label_text)
        
        self.label2_text = StringVar()
        self.label2_text.set(self.correctness)
        self.label2 = Label(master, textvariable=self.label2_text)
    
        #The buttons and format
        self.label.grid(row=0, column=0, columnspan=2, sticky=W+E)
        self.entry.grid(row=1, column=0, columnspan=2, sticky=W+E)
        self.answer_button.grid(row=2, column=1)
        self.label2.grid(row=3, column=0, columnspan=2, sticky=W+E)
        
    def validate(self, input_text):
        if not input_text:
            self.answer = None
            return True
        try:
            self.answer = input_text
            return True
        except ValueError:
            return False
        

    def give_answer(self):
        if self.answer is None:
            self.message = "Comer"

        elif (self.answer).lower() == (self.correct_answer).lower():
            self.correctness="Correct!"
            self.label2_text.set(self.correctness)
            self.reset()
        

        else:
            self.correctness = "Incorrect, it's '" + (self.correct_answer).lower() +"'"
            self.entry.delete(0, END)
            self.answer = ""
        self.label2_text.set(self.correctness)

        
    def reset(self):
        self.entry.delete(0, END)
        self.message = (random.choice(list(WordDict.keys())).strip()).lower()
        self.correct_answer = (WordDict.get(self.message).strip()).lower()
        self.answer = ""

        self.label_text.set(self.message)

        #self.reset_button.configure(state=DISABLED) #turn off reset button
    
            
root = Tk()
my_gui = SpanishFlashcards(root) 
root.mainloop()
