import time
import pyautogui;
import tkinter as tk
from tkinter import *
import pyglet
import sys
import os

#https://stackoverflow.com/questions/31836104/pyinstaller-and-onefile-how-to-include-an-image-in-the-exe-file
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

litery = ["a", "i", "o", "z", "w", "u"]
counter = 5

#logika automatu
def automat():
    guziktimer()
    for item in litery:
        pyautogui.keyDown('ctrl')
        pyautogui.press("h")
        pyautogui.keyUp('ctrl')
        pyautogui.write(f' {item} ')
        pyautogui.press('tab')
        pyautogui.write(f' {item}^s')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('enter')
        pyautogui.press('esc')
    pyautogui.press('esc')

def podwojnie():
    guziktimer()
    i = 1
    while i <= 3:
        pyautogui.keyDown('ctrl')
        pyautogui.press("h")
        pyautogui.keyUp('ctrl')
        pyautogui.write('  ')
        pyautogui.press('tab')
        pyautogui.write(' ')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('enter')
        pyautogui.press('esc')
        pyautogui.keyDown('ctrl')
        pyautogui.press("h")
        pyautogui.keyUp('ctrl')
        pyautogui.write('^p^p')
        pyautogui.press('tab')
        pyautogui.write('^p')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('enter')
        pyautogui.press('esc')
        i += 1
    pyautogui.press('esc')

# guzik timer   

def guziktimer():
    timer.config(text="5 sekund")
    timer.update()
    timer.after(1000, timer.config(text="4 sekundy"))
    timer.update()
    timer.after(1000, timer.config(text="3 sekundy"))
    timer.update()
    timer.after(1000, timer.config(text="2 sekundy"))
    timer.update()
    timer.after(1000, timer.config(text="1 sekunda"))
    timer.update()
    timer.after(1000, timer.config(text="START!"))
    timer.update()
    

pyglet.font.add_file(resource_path("fonts\\Montserrat-VariableFont_wght.ttf"))

#GUI
root = tk.Tk()
root.title("Word Document Formatter 3000")

canvas = tk.Canvas(root, width=600, height=300)
canvas.grid(columnspan=3, rowspan=5)

instruction1 = tk.Label(root, wraplength=350, font="Montserrat", text="Program do wyrzucania pojedynczych literek z ostatnich wersów i pozbywania się podwójnych spacji i enterów")
instruction1.grid(column=1,row=0, padx=20)
instruction2 = tk.Label(root, font="Montserrat", text="Obsługuje litery [a, i, o, z, w, u]")
instruction2.grid(column=1,row=1, padx=20)
instruction3 = tk.Label(root, font="Montserrat", text="Po naciśnięciu guzika masz 5s na wejście w WORDa")
instruction3.grid(column=1,row=2, padx=20)

#działanie guzika
guzik_text = tk.StringVar()
guzikLiterki = tk.Button(root, wraplength=100, textvariable=guzik_text, command=lambda:automat(), width=15, height=3, bg='#a020f0', fg="#fff", font="Montserrat")
guzik_text.set("Wyrzuć pojedyncze litery!")
guzikLiterki.grid(column=1, row=3, padx=(15,200))

timer = tk.Label(root, font="Montserrat", text="")
timer.grid(column=1, row=4)

przerwyText = tk.StringVar()
przerwyText.set("Pozbądź się double spacji i enterów!")
guzikPrzerwy = tk.Button(root, wraplength=110, command=lambda:podwojnie(), textvariable=przerwyText, width=15, height=3, bg='#a020f0', fg="#fff", font="Montserrat")
guzikPrzerwy.grid(column=1, row=3, padx=(200,15))

root.mainloop()