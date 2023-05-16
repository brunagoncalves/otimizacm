import os
from tkinter import *
from tkinter import filedialog, font, messagebox
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
    try:
        width = 340
        height = 340

        files = os.listdir(path_image_folder)
        path_save = path_save_folder
        total_files = len(files)

        for image, file in enumerate(files):
            name_image, extensao = os.path.splitext(file)
            extensao = extensao.lower()

            if extensao in ['.jpg', '.jpeg', '.png']:
                images = Image.open(os.path.join(path_image_folder, file))
                images = images.resize((width, height), Image.LANCZOS)
                images = images.convert('RGB').save(os.path.join(
                    path_save, name_image + '.jpg'), 'JPEG')

            progress_label.config(
                text=f'Redimensionando foto {image+1}/{total_files}')
            app.update()
            progress_label.config(
                text='Fotos (340x340 JPG) redimensionadas com sucesso!')
    except NameError:
        messagebox.showerror(
            "Deu Ruim!", "Você precisa selecionar uma pasta!")
    except ValueError as error:
        messagebox.showerror("Erro", str(error))


def resize_image_mobile():
    try:
        width = 600
        height = 600

        files = os.listdir(path_image_folder)
        path_save = path_save_folder
        total_files = len(files)

        for image, file in enumerate(files):
            if file.endswith('.png'):
                img = Image.open(os.path.join(path_image_folder, file))
                img = img.resize((width, height), Image.LANCZOS)
                img.save(os.path.join(path_save, file))
                progress_label.config(
                    text=f'Redimensionando foto {image+1}/{total_files}')
                app.update()
                progress_label.config(
                    text='Fotos Ipad (600x600) redimensionadas com Sucesso!')
            else:
                messagebox.showerror(
                    'Deu Ruim!', 'Na paste deve conter apenas fotos no formato PNG!')
    except NameError:
        messagebox.showerror(
            "Deu Ruim!", "Você precisa selecionar uma pasta!")
    except ValueError as error:
        messagebox.showerror("Erro", str(error))


def rename_image_report():
    try:
        width = 340
        height = 340

        files = os.listdir(path_image_folder)
        path_save = path_save_folder
        total_files = len(files)

        for image, file in enumerate(files):
            if len(file) == 16 and file.endswith('.png') or len(file) == 16 and file.endswith('.jpg'):
                new_name = file[:10] + file[12:]
            elif len(file) == 17 and file.endswith('.png') or len(file) == 17 and file.endswith('.jpg'):
                new_name = file[:11] + file[13:]
            elif len(file) == 18 and file.endswith('.png') or len(file) == 18 and file.endswith('.jpg'):
                new_name = file[:12] + file[14:]
            elif len(file) == 17 and file.endswith('.jpeg'):
                new_name = file[:10] + file[12:]
            elif len(file) == 18 and file.endswith('.jpeg'):
                new_name = file[:11] + file[13:]
            elif len(file) == 19 and file.endswith('.jpeg'):
                new_name = file[:12] + file[14:]
            else:
                continue

            with Image.open(os.path.join(path_image_folder, file)) as img:
                img = img.resize((width, height), Image.LANCZOS)

                if file.endswith('png'):
                    img.convert('RGB').save(os.path.join(
                        path_save, new_name.replace('.png', '.jpg')))
                elif file.endswith('jpeg'):
                    img.convert('RGB').save(os.path.join(
                        path_save, new_name.replace('.jpeg', '.jpg')))
                else:
                    img.convert('RGB').save(os.path.join(path_save, new_name))

            progress_label.config(
                text=f'Renomeando foto {image+1}/{total_files}')
            app.update()
            progress_label.config(
                text='Fotos (340x340 JPG) renomeadas com sucesso!')
    except NameError:
        messagebox.showerror(
            "Deu Ruim!", "Você precisa selecionar uma pasta!")
    except ValueError as error:
        messagebox.showerror("Erro", str(error))


# Configuration App
app = Tk()
app.title('Otimiza CM - BETA')
app.iconphoto(True, PhotoImage(file='./icons/icon-app.png'))
WIDTH = 500
HEIGHT = 500
screenwidth = app.winfo_screenwidth()
screenheight = app.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (WIDTH, HEIGHT,
                            (screenwidth - WIDTH) / 2, (screenheight - HEIGHT) / 2)
app.geometry(alignstr)
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
    app, text='Qual tarefa você deseja realizar? Clique no botão apenas se tiver certeza!')
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
# progress_bar = ttk.Progressbar(app, orient='horizontal')
# progress_bar.pack(padx=50, pady=10, fill='x')

# Progress label
progress_label = Label(app, text='', fg='green')
progress_label.pack(**ipadding, pady=10)

# Button exit
btn_exit = Button(app, text='  Fechar', image=icon_exit,
                  compound='left', anchor='w', command=app.quit)
btn_exit.pack(**ipadding, pady=10,)

# Author
label_author = Label(app, text='Desenvolvido por Bruna Gonçalves', bg='gray')
label_author.pack(**ipadding, fill='x', expand=True, anchor='s')

app.mainloop()
