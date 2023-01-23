#!/usr/bin/python3
import openai
from openai.error import ServiceUnavailableError
import sys
import os
import docx
from docx import Document
from docx.opc.exceptions import OpcError, PackageNotFoundError
import app
import tkinter
from tkinter.filedialog import askdirectory
from tkinter import Tk
from tkinter import ttk
from tkinter import filedialog
openai.api_key = app.load_key('{}/key.json'.format(sys.path[0]))

#declare globals
directory = None

def main():
    prompt = input('What do you want ChatGPT to do to the docx files? ')
    files = [i for i in os.listdir() if i[-5:] == '.docx']
    for file in files:
        try:
            doc = Document(file)
            rephrase(doc, file, prompt)
        except PackageNotFoundError:
            print('Invalid docx package')
            exit(1)


def rephrase(doc, name, prompt):
    if not isinstance(doc, docx.document.Document):
        raise TypeError('doc must be a valid document object')
    if not isinstance(name, str):
        raise TypeError('name must be a string')
    if not isinstance(prompt, str):
        raise TypeError('prompt must be a string')
    length = len(doc.paragraphs)
    percent = 0
    print('Working on {}...'.format(name))
    for paragraph in doc.paragraphs:
        percent += 1
        print('{}%'.format(int((percent / length) * 100)))
        if len(paragraph.text):
            try:
                text = app.get_result(prompt + paragraph.text)
                paragraph.text = text
            except ServiceUnavailableError:
                print('Error: Server overloaded!')
    doc.save(name)

def make_win():
    win = Tk()
    layout = tkinter.Frame(win, padx=10, pady=10)
    layout.pack(expand=True)
    win.title('GPTChat')
    f_btn = ttk.Button(layout
                ,text='Choose Folder'
                ,command=on_choose
                )
    f_btn.pack()
    prompt = tkinter.Text(layout, padx=10, pady=10)
    prompt.insert('1.0', 'Type your prompt here')
    prompt.pack()
    pg = ttk.Label(layout, text='')
    pg.pack()
    ok_btn = ttk.Button(layout, text='OKAY', width=100)
    ok_btn.pack()
    win.mainloop()

def on_choose():
    directory = filedialog.askdirectory()
    print(directory)
if __name__ == '__main__':
    make_win()
