import os
import shutil
from tkinter import *
from tkinter import filedialog, ttk, font, messagebox
from PIL import Image


def select_image_folder():
    global path_image_folder
    path_image_folder = filedialog.askdirectory()
    label_image_folder.config(text=path_image_folder)


def select_save_folder():
    global path_save_folder
    path_save_folder = filedialog.askdirectory()
    label_save_folder.config(text=path_save_folder)


def resize_image_report():
    width = 340
    height = 340

    files = os.listdir(path_image_folder)
    total_files = len(files)

    progress_label.config(text='Redimensionando imagens')
    progress_bar.config(maximum=total_files)

    for image, file in enumerate(files):
        if file.endswith('.jpg') or file.endswith('.png') or file.endswith('.jpeg'):
            images = Image.open(os.path.join(path_image_folder, file))
            images = images.resize((width, height))
            images.convert('RGB').save(os.path.join(
                path_save_folder, file.replace(".png", ".jpg") or file.replace(".jpeg", ".jpg")))
        progress_bar.step(1)
        progress_label.config(
            text=f'Redimensionando imagem {image+1}/{total_files}')
        window.update()

    progress_label.config(
        text='Redimensionamento relatórios (340x340 JPG) concluído!')


def resize_image_mobile():
    width = 600
    height = 600

    files = os.listdir(path_image_folder)
    total_files = len(files)

    progress_label.config(text='Redimensionando imagens')
    progress_bar.config(maximum=total_files)

    for image, file in enumerate(files):
        if file.endswith('.png'):
            images = Image.open(os.path.join(path_image_folder, file))
            images = images.resize((width, height))
            images.save(os.path.join(path_save_folder, file))
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


def rename_image_report():
    width = 340
    height = 340

    files = os.listdir(path_image_folder)
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

        shutil.copy2(os.path.join(path_image_folder, file),
                     os.path.join(path_save_folder, new_name))
        new_name.resize((width, height)).convert('RGB').save(
            os.path.join(path_save_folder, file.replace(".png", ".jpg")))
        progress_bar.step(1)
        progress_label.config(
            text=f'Renomeando imagens {image+1}/{total_files}')
        window.update()
        progress_label.config(text='Imagens renomeadas com sucesso!')


# Create window tkinter
window = Tk()
window.title('OtimizaCM')
window.iconphoto(True, PhotoImage(file='./icons/icon-app.png'))
WIDTH = 600
HEIGHT = 600
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
screen_center = '%dx%d+%d+%d' % (WIDTH, HEIGHT,
                                 (screen_width - WIDTH) / 2, (screen_height - HEIGHT) / 2)
window.geometry(screen_center)
window.resizable(0, 0)

# Icons
icon_folder = PhotoImage(file='./icons/folder-open.png')
icon_exit = PhotoImage(file='./icons/exit.png')
icon_resize = PhotoImage(file='./icons/resize.png')

# Set default font
font_default = font.Font(family='Helvetica', size=9, weight='bold')
font.families()
window.option_add('*Font', font_default)

# Styles
ipadding = {'ipadx': 5, 'ipady': 5}
padding = {'padx': 10, 'pady': 5}

# Label info image folder
label_info_folder = Label(
    window, text='Onde esta a pasta para Redimensionar ou Renomear?', justify='left')
label_info_folder.place(x=10, y=10)

label_info_folder = Label(
    window, text='Em que pasta deseja salvar as imagens?', justify='left')
label_info_folder.place(x=10, y=86)

# Button select image folder
btn_image_folder = Button(window, image=icon_folder,
                          command=select_image_folder)
btn_image_folder.place(x=10, y=40, width=40, height=40)

label_image_folder = Label(window, text='', justify='left', bg='#fff18c')
label_image_folder.place(x=60, y=47)

# Button select save folder
btn_save_folder = Button(window, image=icon_folder, command=select_save_folder)
btn_save_folder.place(x=10, y=117, width=40, height=40)

label_save_folder = Label(window, text='', justify='left', bg='#fff18c')
label_save_folder.place(x=60, y=124)

# Label info button resize and rename
label_info_btn = Label(window, text='Escolha a tarefa a ser realizada.')
label_info_btn.place(x=10, y=164)

# Buttons
btn_resize_report = Button(
    window, text='Redimensionar fotos paea relatórios (340x340 JPG)', command=resize_image_report)
btn_resize_report.place(x=10, y=195)

btn_resize_mobile = Button(
    window, text='Redimensionar fotos paea relatórios (340x340 JPG)', command=resize_image_mobile)
btn_resize_mobile.place(x=10, y=230)

btn_rename_report = Button(
    window, text='Redimensionar fotos paea relatórios (340x340 JPG)', command=rename_image_report)
btn_rename_report.place(x=10, y=266)

# Progress Bar
progress_bar = ttk.Progressbar(window, orient='horizontal')
progress_bar.place(x=10, y=320)

# Progress label
progress_label = Label(window, text='')
progress_label.place(x=10, y=370)

# Author
label_author = Label(window, text='Desenvolvido por Bruna Gonçalves')
label_author.place(x=10, y=400)

# Start screen
window.mainloop()
