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
    progress_bar.config(maximum=total_files)

    for image, file in enumerate(files):
        name_image, extensao = os.path.splitext(file)
        extensao = extensao.lower()

        if extensao in ['.jpg', '.jpeg', '.png']:
            images = Image.open(os.path.join(path_image_folder, file))
            images = images.resize((width, height), Image.LANCZOS)
            images = images.convert('RGB').save(os.path.join(
                path_save_folder, name_image + '.jpg'), 'JPEG')

        progress_bar.step(1)
        progress_label.config(
            text=f'Redimensionando foto {image+1}/{total_files}')
        app.update()
        progress_label.config(
            text='Fotos (340x340 JPG) redimensionadas com sucesso!')


def resize_image_mobile():
    width = 600
    height = 600

    files = os.listdir(path_image_folder)
    total_files = len(files)
    progress_bar.config(maximum=total_files)

    for image, file in enumerate(files):
        if file.endswith('.png'):
            images = Image.open(os.path.join(path_image_folder, file))
            images = images.resize((width, height), Image.LANCZOS)
            images.save(os.path.join(path_save_folder, file))
            progress_bar.step(2)
            progress_label.config(
                text=f'Redimensionando foto {image+1}/{total_files}')
            app.update()
            progress_label.config(
                text='Fotos Ipad (600x600) redimensionadas com Sucesso!')
        else:
            messagebox.showerror(
                'Deu Ruim!', 'Para redimensionar (600x600 PNG), na pasta só deve conter fotos em formato PNG!')
            break


def rename_image_report():
    width = 340
    height = 340

    files = os.listdir(path_image_folder)
    total_files = len(files)
    progress_bar.config(maximum=total_files)

    for image, file in enumerate(files):
        path_image = os.path.join(path_image_folder, file)

        if len(file) == 16:
            new_name = file[:10] + file[12:]
        elif len(file) == 17:
            new_name = file[:11] + file[13:]
        elif len(file) == 18:
            new_name = file[:12] + file[14:]
        else:
            continue

        novo_caminho = os.path.join(path_image_folder, new_name)

        with Image.open(path_image) as img:
            img = img.resize((width, height))
            img = img.convert('RGB')
            img.save(novo_caminho, 'JPEG')

        # shutil.copy2(os.path.join(path_image_folder, file),
        #              os.path.join(path_save_folder, new_name))
        # images = new_name.resize((width, height))
        # images = images.convert('RGB').save(os.path.join(
        #     path_save_folder, file.replace(".png", ".jpg")))

        progress_bar.step(1)
        progress_label.config(text=f'Renomeando foto {image+1}/{total_files}')
        app.update()
        progress_label.config(
            text='Fotos (340x340 JPG) renomeadas com sucesso!')


# Configuration App
app = Tk()
app.title('Otimiza CM - BETA')
app.iconphoto(True, PhotoImage(file='./icons/icon-app.png'))
app.geometry('500x470')
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

# Label information select folder image
laber_info_folder = Label(
    app, text='Selecione a pasta onde estão as fotos para redimensionar.')
laber_info_folder.pack(**ipadding, anchor='w')

frame_image_folder = Frame(app)
frame_image_folder.pack(fill='x', ipady=5, padx=10)

# Button select image folder
btn_image_folder = Button(
    frame_image_folder, image=icon_folder, command=select_image_folder)
btn_image_folder.pack(**ipadding, side='left', padx=(10, 0))

# Label information select folder save
laber_info_folder = Label(
    app, text='Selecione a pasta onde deseja salvar as fotos.')
laber_info_folder.pack(**ipadding, anchor='w')

frame_save_folder = Frame(app)
frame_save_folder.pack(fill='x', ipady=5, padx=10)

# Button select save folder
btn_save_folder = Button(
    frame_save_folder, image=icon_folder, command=select_save_folder)
btn_save_folder.pack(**ipadding, side='left', padx=(10, 0))

# Label image folder
label_image_folder = Label(
    frame_image_folder, text='', bg='#fff18c', fg='green', anchor='w')
label_image_folder.pack(**ipadding, fill='x', expand=True, padx=10, pady=3)

# Label save folder
label_save_folder = Label(
    frame_save_folder, text='', bg='#fff18c', fg='green', anchor='w')
label_save_folder.pack(**ipadding, fill='x', expand=True, padx=10, pady=3)

# Select the task
label_task = Label(
    app, text='Para realizar uma terefa, clique no botão.')
label_task.pack(**ipadding, anchor='w')

# Buttons select task
frame_action = Frame(app)
frame_action.pack()

btn_resize_report = Button(
    frame_action, text='  Redimensionar fotos para relatórios (340x340 JPG)', image=icon_resize, compound='left', command=resize_image_report, anchor='w')
btn_resize_report.pack(**ipadding, fill='x', pady=5)

btn_resize_mobile = Button(
    frame_action, text='  Redimensionar fotos para Ipad (600x600 PNG)', image=icon_resize, compound='left', command=resize_image_mobile, anchor='w')
btn_resize_mobile.pack(**ipadding, fill='x', pady=5)

btn_rename_report = Button(
    frame_action, text='  Renomear fotos para relatórios (340x340 JPG)', image=icon_resize, compound='left', command=rename_image_report, anchor='w')
btn_rename_report.pack(**ipadding, fill='x', pady=5)

# Progress Bar
progress_bar = ttk.Progressbar(app, orient='horizontal')
progress_bar.pack(padx=50, pady=10, fill='x')

# Progress label
progress_label = Label(app, text='', fg='green')
progress_label.pack(**ipadding, pady=10)

# Author
label_author = Label(app, text='Desenvolvido por Bruna Gonçalves', bg='gray')
label_author.pack(**ipadding, fill='x', expand=True)

app.mainloop()
