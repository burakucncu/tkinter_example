import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk
import pygame
import random
from tkinter import filedialog
from PIL import Image, ImageTk

# You can change the text parts as you wish.

def yes():
    pygame.mixer.init()
    pygame.mixer.music.load('mcqueen-kachow.mp3')
    pygame.mixer.music.play()
    result_label.config(text='SONUNDA BE ASK KARI!')


change_x_no = 425
change_y_no = 300
change_x_yes = 375
change_y_yes = 300
no_meter = 0
exit_button = None

def no():
    global change_x_no, change_y_no, change_x_yes, change_y_yes, no_meter, exit_button
    change_x_no = random.randint(70, 750)
    change_y_no = random.randint(70, 500)
    change_x_yes = change_x_no - 50
    change_y_yes = change_y_no
    no_button.place(x=change_x_no, y=change_y_no)
    yes_button.place(x=change_x_yes, y=change_y_yes)
    no_meter += 1
    if no_meter == 5:
        result_label.config(text='Sevsene canim')
    elif no_meter == 10:
        result_label.config(text='Sevsene')
    elif no_meter == 20:
        result_label.config(text='Sevmedin mi hâlâ ag?')
    elif no_meter == 25:
        no_meter = 0
    else:
        result_label.config(text='')
    
    if no_meter == 7 or no_meter == 15:
        result_label.config(text='sevmezsen sevme sağ aşağı çıkış butonu koydum bas git')
        if exit_button is None:
            exit_button = ttk.Button(window,
                                    text='Exit',
                                    command=exit)
            exit_button.place(x=750, y=560)
    else:
        if exit_button is not None:
            exit_button.destroy()
            exit_button = None

def exit():
    global no_meter
    if no_meter == 7:
        result_label.config(text='Kandırdım bebiş kıps ;)')
        pygame.mixer.init()
        pygame.mixer.music.load('Kandirdim.mp3')
        pygame.mixer.music.play()
    elif no_meter == 15:
        result_label.config(text='Eee gene kandırdım senı bebiş kıps ;)')
        pygame.mixer.init()
        pygame.mixer.music.load('Kandirdim.mp3')
        pygame.mixer.music.play()

# Window
window = ttk.Style().master
window.title('Are You Love Me?')
window.geometry('800x600')

background_image = Image.open('mcquenn_sally.jpg')
background_image = background_image.resize((800, 600), Image.LANCZOS)
background_photo = ImageTk.PhotoImage(background_image)
background_label = ttk.Label(window, image=background_photo)
background_label.place(relwidth=1, relheight=1)


window_label = ttk.Label(window, 
                         text='Are You Love Me?', 
                         font=('Times 24 bold italic'),
                         foreground='red')
window_label.pack(pady=20)



# Yes Button

input_frame_yes = ttk.Frame(window)
yes_button = ttk.Button(window, 
                        text='Yes',
                        command=yes)
yes_button.place(x=change_x_yes, y=change_y_yes)

# No Button

input_frame_no = ttk.Frame(window)
no_button = ttk.Button(window,
                       text='No',
                       command=no)
no_button.place(x=change_x_no, y=change_y_no)


# Result

result_label = ttk.Label(window, 
                         text='', 
                         font=('Times 16 bold italic'),
                         foreground='blue')
result_label.pack(side='bottom', pady=20)

# Run

window.mainloop()