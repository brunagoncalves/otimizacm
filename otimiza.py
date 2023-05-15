import os
from tkinter import *
from tkinter import filedialog, font


def select_image_folder():
    global path_image_folder
    path_image_folder = filedialog.askdirectory()
    label_image_folder.config(path_image_folder)


def select_save_folder():
    global path_save_folder
    path_save_folder = filedialog.askdirectory()
    label_save_folder.config(path_save_folder)


# Configuration App
app = Tk()
app.title('Otimiza CM - BETA')
app.iconphoto(True, PhotoImage(file='./icons/icon-app.png'))
app.geometry('500x600')
app.resizable(False, False)

# Icons
icon_folder = PhotoImage(file='./icons/folder-open.png')
icon_exit = PhotoImage(file='./icons/exit.png')
icon_resize = PhotoImage(file='./icons/resize.png')

# Set default font
font_default = font.Font(family='Helvetica', size=9, weight='bold')
font.families()
app.option_add('*Font', font_default)

# Styles
ipadding = {'ipadx': 5, 'ipady': 5}
padding = {'padx': 10, 'pady': 5}

frame_image_folder = Frame(app)
frame_image_folder.pack(fill='x')

frame_save_folder = Frame(app)
frame_save_folder.pack(fill='x')

# Button select image folder
btn_image_folder = Button(
    frame_image_folder, image=icon_folder, command=select_image_folder)
btn_image_folder.pack(**ipadding, **padding, side='left')

# Button select save folder
btn_save_folder = Button(
    frame_save_folder, image=icon_folder, command=select_save_folder)
btn_save_folder.pack(**ipadding, **padding, side='left')

# Label image folder
label_image_folder = Label(
    frame_image_folder, text='Caminho selecionado é', bg='#fff18c')
label_image_folder.pack(**ipadding, **padding,
                        expand=True, anchor='w')

# Label save folder
label_save_folder = Label(
    frame_save_folder, text='Caminho selecionado é', bg='#fff18c')
label_save_folder.pack(**ipadding, **padding,
                       expand=True, anchor='w')

# Select the task
label_task = Label(
    app, text='Clique no botão que corresponde a tarefa a ser realizada.')
label_task.pack(**ipadding, **padding, anchor='w')

app.mainloop()
