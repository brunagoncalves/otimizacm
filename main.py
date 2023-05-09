import os
from tkinter import *
from tkinter import filedialog, ttk, font
from PIL import Image


def select_path_image():
    global path_folder_image
    path_folder_image = filedialog.askdirectory()
    label_path_folder_image.config(text=path_folder_image)


def select_path_save():
    global path_folder_save
    path_folder_save = filedialog.askdirectory()
    label_path_folder_save.config(text=path_folder_save)


def resize_image_report():
    width = int(width_entry.get())
    height = int(height_entry.get())

    files = os.listdir(path_folder_image)
    total_files = len(files)

    progress_label.config(text=f'Redimensionando imagens para relatórios')
    progress_bar.config(maximum=total_files)

    for image, file in enumerate(files):
        if file.endswith(".jpg") or file.endswith(".png"):
            images = Image.open(os.path.join(path_folder_image, file))
            images = images.resize((width, height))
            images.convert('RGB').save(os.path.join(
                path_folder_save, file.replace(".png", ".jpg")))
        progress_bar.step(1)
        progress_label.config(
            text=f'Redimensionando imagem {image+1}/{total_files}')
        window.update()

    progress_label.config(text=f'Redimensionamento relatórios concluído!')


def resize_image_ipad():
    width = int(width_entry.get())
    height = int(height_entry.get())

    files = os.listdir(path_folder_image)
    total_files = len(files)

    progress_label.config(text=f'Redimensionando imagens para Ipad')
    progress_bar.config(maximum=total_files)

    for image, file in enumerate(files):
        if file.endswith(".png"):
            images = Image.open(os.path.join(path_folder_image, file))
            images = images.resize((width, height))
            images.save(os.path.join(path_folder_save, file))
        progress_bar.step(1)
        progress_label.config(
            text=f'Redimensionando imagem {image+1}/{total_files}')
        window.update()

    progress_label.config(text=f'Redimensionamento Ipad concluído!')


# Create screen
window = Tk()
window.iconphoto(False, PhotoImage(file='./icons/icon-app.png'))
window.title('CM Otimiza - BETA')
window.geometry('500x550')
window.resizable(False, False)

# Variables
ipadding = {'ipadx': 3, 'ipady': 3}
padd_button = {'padx': 30, 'pady': 5}

# Fonts
font_bold = font.Font(
    size=9,
    weight='bold'
)

# Icons
icon_folder = PhotoImage(file='./icons/folder-open.png')
icon_exit = PhotoImage(file='./icons/exit.png')
icon_resize = PhotoImage(file='./icons/resize.png')

# Select folder image
btn_path_image = Button(
    window,
    image=icon_folder,
    text='  O que você quer redimensionar?',
    compound='left',
    font=font_bold,
    command=select_path_image
)

btn_path_image.pack(**ipadding, padx=30, pady=(15, 5), fill='x')

# Label folder images
label_path_folder_image = Label(
    window,
    text='',
    bg='white',
    fg='green',
    font=font_bold
)

label_path_folder_image.pack(**ipadding, **padd_button, fill='x')

# Select folder save
btn_path_image = Button(
    window,
    image=icon_folder,
    text='  Onde deseja salvar?',
    compound='left',
    font=font_bold,
    command=select_path_save
)

btn_path_image.pack(**ipadding, **padd_button, fill='x')

# Label folder save
label_path_folder_save = Label(
    window,
    text='',
    bg='white',
    fg='green',
    font=font_bold
)

label_path_folder_save.pack(**ipadding, **padd_button, fill='x')

# Label size
width_label = Label(window, text='Largura')
width_label.pack(**ipadding, **padd_button)

# Entry size
width_entry = Entry(window, font=font_bold, justify='center')
width_entry.pack(**ipadding, **padd_button)

# Label size
height_label = Label(window, text='Altura')
height_label.pack(**ipadding, **padd_button)

# Entry size
height_entry = Entry(window, font=font_bold, justify='center')
height_entry.pack(**ipadding, **padd_button)

# Button resize
btn_resize = Button(
    window,
    image=icon_resize,
    text='  Redimensionar para Relatórios',
    font=font_bold,
    compound='left',
    command=resize_image_report
)

btn_resize.pack(**ipadding, **padd_button, fill='x')

# Button resize ipad
btn_resize = Button(
    window,
    image=icon_resize,
    text='  Redimensionar para Ipad',
    font=font_bold,
    compound='left',
    command=resize_image_ipad
)

btn_resize.pack(**ipadding, **padd_button, fill='x')

# Progress Bar
progress_bar = ttk.Progressbar(window, orient='horizontal')
progress_bar.pack(**padd_button, fill='x')

# Progress label
progress_label = Label(
    window,
    text='',
    fg='green',
    font=font_bold
)
progress_label.pack(**ipadding, **padd_button)

# Button exit
btn_exit = Button(
    window,
    image=icon_exit,
    text='  Fechar',
    compound='left',
    font=font_bold,
    fg='red',
    command=window.quit)

btn_exit.pack(**ipadding, **padd_button)

# Start window
window.mainloop()
