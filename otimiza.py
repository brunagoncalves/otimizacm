""" Imports """
import os  # Allows access to operating system functionality
import tkinter
from tkinter import filedialog, font, messagebox
from PIL import Image  # Pillow - Lets you open, manipulate and save images


def clean_error():
    """ Clear the error message """
    progress_label_error.config(text="")


PATH_FOLDER_IMAGE: str
PATH_SAVE_FOLDER: str


def select_folder_image():
    """ Function to select source path """
    global PATH_FOLDER_IMAGE
    PATH_FOLDER_IMAGE = filedialog.askdirectory()
    label_image_folder.config(text=PATH_FOLDER_IMAGE)


def select_folder_save():
    """ Function to select destination path """
    global PATH_SAVE_FOLDER
    PATH_SAVE_FOLDER = filedialog.askdirectory()
    label_save_folder.config(text=PATH_SAVE_FOLDER)


def resize_image_report():
    """ Function to resize photos 340x340 """
    clean_error()
    try:
        width = 340
        height = 340

        files = os.listdir(PATH_FOLDER_IMAGE)
        path_save = PATH_SAVE_FOLDER
        total_files = len(files)

        for image, file in enumerate(files):
            name_image, extensao = os.path.splitext(file)
            extensao = extensao.lower()

            if extensao in ['.jpg', '.jpeg', '.png']:
                images = Image.open(os.path.join(PATH_FOLDER_IMAGE, file))
                images = images.resize((width, height), Image.LANCZOS)
                images = images.convert('RGB').save(os.path.join(
                    path_save, name_image + '.jpg'), 'JPEG')

            progress_label.config(
                text=f'Redimensionando foto {image+1}/{total_files}')
            app.update()
            progress_label.config(
                text='Fotos (340x340 JPG) redimensionadas com SUCESSO!')
    except NameError:
        messagebox.showerror(
            'Deu Ruim!', 'Ops! Você não selecionou uma pasta!')
    except ValueError as error:
        messagebox.showerror("Erro", str(error))


def resize_image_mobile():
    """ Function to resize photos 600x600 """
    clean_error()

    messagebox.askyesno(
        "Mensagem de Informação",
        "Caso tenha selecionado a mesma pasta para salvar, as fotos originais serão substituidas! Deseja continuar?")
    try:
        width = 600
        height = 600

        files = os.listdir(PATH_FOLDER_IMAGE)
        path_save = PATH_SAVE_FOLDER
        total_files = len(files)

        for image, file in enumerate(files):
            if file.endswith('.png'):
                img = Image.open(os.path.join(PATH_FOLDER_IMAGE, file))
                img = img.resize((width, height), Image.LANCZOS)
                img = img.save(os.path.join(path_save, file))
                progress_label.config(
                    text=f'Redimensionando foto {image+1}/{total_files}')
                app.update()
                progress_label.config(
                    text='Fotos Ipad (600x600 PNG) redimensionadas com SUCESSO!')
            else:
                messagebox.showerror(
                    'Deu Ruim!', 'Apenas fotos no formato PNG são aceitas!')
                progress_label_error.config(
                    text='Verifique se deu tudo certo!')
                break
    except NameError:
        messagebox.showerror(
            'Deu Ruim!', 'Ops! Você não selecionou uma pasta!')
    except ValueError as error:
        messagebox.showerror("Erro", str(error))


def rename_image_report():
    """ Function to resize 340x340 photos and rename """
    clean_error()
    try:
        width = 340
        height = 340

        files = os.listdir(PATH_FOLDER_IMAGE)
        path_save = PATH_SAVE_FOLDER
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

            with Image.open(os.path.join(PATH_FOLDER_IMAGE, file)) as img:
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
                text='Fotos (340x340 JPG) renomeadas com SUCESSO!')
    except NameError:
        messagebox.showerror(
            'Deu Ruim!', 'Ops! Você não selecionou uma pasta!')
    except ValueError as error:
        messagebox.showerror("Erro", str(error))


def negative_image_stock():
    """ Function to convert photos to negative """
    clean_error()
    try:
        files = os.listdir(PATH_FOLDER_IMAGE)
        path_save = PATH_SAVE_FOLDER
        total_files = len(files)

        for image, file in enumerate(files):
            img = Image.open(os.path.join(PATH_FOLDER_IMAGE, file))
            img = img.convert("L")
            img.save(os.path.join(path_save, file))

            progress_label.config(
                text=f'Editando fotos {image+1}/{total_files}')
            app.update()
            progress_label.config(
                text='fotos editadas com SUCESSO!')
    except NameError:
        messagebox.showerror(
            'Deu Ruim!', 'Ops! Você não selecionou uma pasta!')
    except ValueError as error:
        messagebox.showerror("Erro", str(error))


# Configuration App
app = tkinter.Tk()
app.title('OtimizaCM')
app.iconphoto(True, tkinter.PhotoImage(file='./icons/icon-app.png'))

WIDTH = 650
HEIGHT = 750
screenwidth = app.winfo_screenwidth()
screenheight = app.winfo_screenheight()
alignstr = f"{WIDTH}x{HEIGHT}+{(screenwidth - WIDTH) // 2}+{(screenheight - HEIGHT) // 2}"
app.geometry(alignstr)
app.resizable(False, False)

# Set default font
font_default = font.Font(family='Segoe UI', size=10, weight='normal')
font_bold = font.Font(family='Segoe UI', size=10, weight='bold')
app.option_add('*Font', font_default)

# Icons
icon_close = tkinter.PhotoImage(file='./icons/close.png')
icon_convert = tkinter.PhotoImage(file='./icons/convert.png')
icon_resize = tkinter.PhotoImage(file='./icons/resize.png')
icon_rename = tkinter.PhotoImage(file='./icons/rename.png')
icon_folder = tkinter.PhotoImage(file='./icons/open-folder.png')
icon_picture = tkinter.PhotoImage(file='./icons/picture.png')

# Label information select folder
label_info_folder = tkinter.Label(
    app, text="Selecione a pasta onde estão as fotos para redimensionar.")
label_info_folder.pack(padx=20, pady=(10, 0), anchor='w')

frame_image_folder = tkinter.Frame(app)
frame_image_folder.pack(fill='x', ipady=10, padx=10)

# Button select folder
btn_select_folder = tkinter.Button(
    frame_image_folder, image=icon_folder, command=select_folder_image)
btn_select_folder.pack(side='left', padx=(10, 0), ipadx=5, ipady=5)

# Label information select folder save
label_info_folder = tkinter.Label(
    app, text="Selecione a pasta onde deseja salvar as fotos.")
label_info_folder.pack(padx=20, pady=5, anchor='w')

frame_save_folder = tkinter.Frame(app)
frame_save_folder.pack(fill='x', ipady=5, padx=10)

# Button select save folder
btn_save_folder = tkinter.Button(
    frame_save_folder, image=icon_folder, command=select_folder_save)
btn_save_folder.pack(side='left', padx=(10, 0), ipadx=5, ipady=5)

# Label image folder
label_image_folder = tkinter.Label(
    frame_image_folder,
    text='',
    bg='#D8D9DA',
    fg='blue',
    anchor='w',
    font=font_bold,
    padx=5)
label_image_folder.pack(
    pady=5,
    fill='x',
    expand=True,
    padx=10,
    ipady=8,
    ipadx=3)

# Label save folder
label_save_folder = tkinter.Label(
    frame_save_folder,
    text='',
    bg='#D8D9DA',
    fg='blue',
    anchor='w',
    font=font_bold,
    padx=5)
label_save_folder.pack(
    fill='x',
    expand=True,
    padx=10,
    ipady=8,
    ipadx=3)

# Select the task
label_task = tkinter.Label(
    app, text="Qual tarefa você deseja realizar? Clique no botão apenas se tiver certeza!")
label_task.pack(padx=20, pady=10, anchor='w')

# Buttons selecting the task
frame_action = tkinter.Frame(app)
frame_action.pack()

btn_resize_report = tkinter.Button(
    frame_action,
    text="  Redimensionar fotos 340x340 JPG (Relatórios)",
    image=icon_resize,
    compound='left',
    command=resize_image_report,
    anchor='w',
    padx=10,
    pady=10)
btn_resize_report.pack(padx=5, fill='x', pady=5)

btn_resize_mobile = tkinter.Button(
    frame_action,
    text="  Redimensionar fotos 600x600 PNG (Ipad)",
    image=icon_resize,
    compound='left',
    command=resize_image_mobile,
    anchor='w',
    padx=10,
    pady=10)
btn_resize_mobile.pack(padx=5, fill='x', pady=5)

btn_rename_report = tkinter.Button(
    frame_action,
    text="  Renomear e redimencionar fotos 340x340 JPG (Relatórios)",
    image=icon_rename,
    compound='left',
    command=rename_image_report,
    anchor='w',
    padx=10,
    pady=10)
btn_rename_report.pack(padx=5, pady=5, fill='x')

btn_convert_negative = tkinter.Button(
    frame_action,
    text="  Converter fotos para negativo",
    image=icon_convert,
    compound='left',
    command=negative_image_stock,
    anchor='w',
    padx=10,
    pady=10)
btn_convert_negative.pack(padx=5, pady=5, fill='x')

# Progress label Ok
progress_label = tkinter.Label(app, text='', fg='green')
progress_label.pack(padx=5, pady=10)

# Progress label Error
progress_label_error = tkinter.Label(app, text='', fg='red')
progress_label_error.pack(padx=5, pady=10)

# Button exit
btn_exit = tkinter.Button(
    app,
    text=' Fechar',
    image=icon_close,
    compound='left',
    anchor='w',
    command=app.quit,
    padx=10,
    pady=10,
    font=font_bold)
btn_exit.pack(padx=5, pady=10,)

# Author
label_author = tkinter.Label(
    app,
    text="Desenvolvido por Bruna Gonçalves",
    font=font_bold,
    padx=10,
    pady=10,
    bg='#D8D9DA')
label_author.pack(fill='x', expand=True, anchor='s')

app.mainloop()
