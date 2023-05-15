import os
from tkinter import *
from tkinter import filedialog, font, ttk
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
        name_image, extensao = os.path.splitext(file)
        extensao = extensao.lower()

        if file in ['.jpg', '.jpeg', '.png']:
            images = Image.open(os.path.join(path_image_folder, file))
            images = images.resize((width, height), Image.ANTIALIAS)
            images = images.convert('RGB').save(os.path.join(path_save_folder, name_image + 'jpg'), 'JPEG')

        progress_bar.step(1)
        progress_label.config(
            text=f'Redimensionando imagem {image+1}/{total_files}')
        app.update()
        progress_label.config(
            text='Redimensionamento relatórios (340x340 JPG) concluído!')


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

# Label information select folder
laber_info_folder = Label(
    app, text='Clique no botão abaixo para selecionar os diretórios.')
laber_info_folder.pack(**ipadding, **padding, anchor='w')

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
    frame_image_folder, text='', bg='#fff18c')
label_image_folder.pack(**ipadding, **padding, expand=True, fill='both')

# Label save folder
label_save_folder = Label(
    frame_save_folder, text='', bg='#fff18c')
label_save_folder.pack(**ipadding, **padding, expand=True, fill='both')

# Select the task
label_task = Label(
    app, text='Clique no botão que corresponde a tarefa a ser realizada.')
label_task.pack(**ipadding, **padding, anchor='w')

# Buttons select task
btn_resize_report = Button(
    app, text='Redimensionar fotos para relatórios (340x340 JPG)', command=resize_image_report)
btn_resize_report.pack(**ipadding, **padding)

btn_resize_mobile = Button(
    app, text='Redimensionar fotos para Ipad (600x600 PNG)')
btn_resize_mobile.pack(**ipadding, **padding)

btn_rename_report = Button(
    app, text='Renomear fotos para relatórios (340x340 JPG)')
btn_rename_report.pack(**ipadding, **padding)

# Progress Bar
progress_bar = ttk.Progressbar(app, orient='horizontal')
progress_bar.pack()

# Progress label
progress_label = Label(app, text='')
progress_label.pack(**ipadding, **padding)

app.mainloop()
