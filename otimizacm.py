import os
import shutil
from tkinter import *
from tkinter import filedialog, ttk, font, messagebox
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
    width = 340
    height = 340

    files = os.listdir(path_folder_image)
    total_files = len(files)

    progress_label.config(text='Redimensionando imagens')
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

    progress_label.config(
        text='Redimensionamento relatórios (340x340 JPG) concluído!')


def resize_image_ipad():
    width = 600
    height = 600

    files = os.listdir(path_folder_image)
    total_files = len(files)

    progress_label.config(text='Redimensionando imagens')
    progress_bar.config(maximum=total_files)

    for image, file in enumerate(files):
        if file.endswith('.png'):
            images = Image.open(os.path.join(path_folder_image, file))
            images = images.resize((width, height))
            images.save(os.path.join(path_folder_save, file))
            progress_bar.step(2)
            progress_label.config(
                text=f'Redimensionando imagem {image+1}/{total_files}')
            
            window.update()
            progress_label.config(
                text='Redimensionamento Ipad Ipad (600x600 PNG) concluído!')
        else:
            messagebox.showerror(
                'Deu Ruim!', 'Na pasta contém imagens JPG, e não podem ser redimensionadas, o Ipad aceita apenas PNG!')
            break


def rename_image():
    files = os.listdir(path_folder_image)
    total_files = len(files)

    progress_label.config(text='Redimensionando imagens')
    progress_bar.config(maximum=total_files)

    for image, file in enumerate(files):
        if len(file) == 16:
            new_name = file[:10] + file[12:]
        elif len(file) == 17:
            new_name = file[:11] + file[13:]
        elif len(file) == 18:
            new_name = file[:12] + file[14:]
        else:
            continue

        shutil.copy2(os.path.join(path_folder_image, file),os.path.join(path_folder_save, new_name))
        progress_bar.step(1)
        progress_label.config(text=f'Renomeando imagens {image+1}/{total_files}')
        window.update()
        progress_label.config(text='Imagens renomeadas com sucesso!')


# Create screen
window = Tk()
window.iconphoto(False, PhotoImage(file='./icons/icon-app.png'))
window.title('CM Otimiza - BETA')
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 580
w = int((screen_width - WINDOW_WIDTH) / 2)
h = int((screen_height - WINDOW_HEIGHT) / 2)
window.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{w}+{h}')
window.resizable(False, False)

# Variables
ipadding = {'ipadx': 3, 'ipady': 3}
padd_button = {'padx': 30, 'pady': 10}

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
    bg='#fff18c',
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
    bg='#fff18c',
    fg='green',
    font=font_bold
)

label_path_folder_save.pack(**ipadding, **padd_button, fill='x')

# Button resize
btn_resize = Button(
    window,
    image=icon_resize,
    text='  Redimensionar para Relatórios/Pronta Entrega (340x340 JPG)',
    font=font_bold,
    compound='left',
    command=resize_image_report
)

btn_resize.pack(**ipadding, **padd_button, fill='x')

# Button resize ipad
btn_resize = Button(
    window,
    image=icon_resize,
    text='  Redimensionar para Ipad (600x600 PNG)',
    font=font_bold,
    compound='left',
    command=resize_image_ipad
)

btn_resize.pack(**ipadding, **padd_button, fill='x')

# Button rename
btn_rename = Button(
    window,
    image=icon_resize,
    text='  Renomear imagens para Relatórios/Pronto Entrega',
    font=font_bold,
    compound='left',
    command=rename_image
)

btn_rename.pack(**ipadding, **padd_button, fill='x')

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

# Informations
label_author = Label(
    window,
    text='Desenvolvido por Bruna Gonçalves',
    bg='#413d3d',
    fg='white',
    font=font_bold
)

label_author.pack(
    ipady=3,
    pady=(10, 0),
    anchor='s',
    expand=True,
    fill='x'
)

# Start window
window.mainloop()
