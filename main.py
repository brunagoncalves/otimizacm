import os
from tkinter import Tk, filedialog, ttk, Label, Button, Entry, PhotoImage
from PIL import Image


def select_path_images():
    global path_images
    path_images = filedialog.askdirectory()
    label_path_images.config(text=path_images)


def select_path_save():
    global path_save
    path_save = filedialog.askdirectory()
    label_path_save.config(text=path_save)


def resize_images():
    global width
    global height
    width = int(width_entry.get())
    height = int(height_entry.get())

    files = os.listdir(path_images)
    total_files = len(files)

    progress_label.config(text=f"Redimensionando imagens...")
    progress_bar.config(maximum=total_files)

    for image, file in enumerate(files):
        if file.endswith(".png"):
            images = Image.open(os.path.join(path_images, file))
            images = images.resize((width, height))
            images.convert('RGB').save(os.path.join(
                path_save, file.replace(".png", ".jpg")))
        progress_bar.step(1)
        progress_label.config(
            text=f"Redimensionando imagem {image+1}/{total_files}")
        window.update()

    progress_label.config(text=f"Redimensionamento concluído!")


# Create screen
window = Tk()
window.title('CM Otimiza - BETA')
window.geometry("600x600")

# Define icons
folder_open = PhotoImage(file='./icons/folder-open.png')

# Button select path
btn_path_image = Button(
    window,
    image=folder_open,
    compound='center',
    command=select_path_images
)

btn_path_image.grid(
    row=0,
    column=0,
    padx=5,
    pady=3,
    ipadx=3,
    ipady=3
)

btn_path_save = Button(
    window,
    image=folder_open,
    compound='center',
    command=select_path_save
)

btn_path_save.grid(
    row=2,
    column=0,
    padx=5,
    pady=3,
    ipadx=3,
    ipady=3
)

# Label select path
label_path_images = Label(
    window,
    text=''
)

label_path_images.grid(
    row=0,
    column=1,
    padx=10,
    pady=5
)

label_path_save = Label(
    window,
    text=''
)

label_path_save.grid(
    row=2,
    column=1,
    padx=10,
    pady=5
)

# Entry Width - Height
width_label = Label(window, text="Largura:")

width_label.grid(
    row=3,
    column=1
)

width_entry = Entry(window)

width_entry.grid(
    row=3,
    column=2
)

height_label = Label(window, text="Altura:")

height_label.grid(
    row=4,
    column=1
)

height_entry = Entry(window)

height_entry.grid(
    row=4,
    column=2
)

# Button resize
btn_resize = Button(
    window,
    text='Redimensionar Imagens',
    command=resize_images
)

btn_resize.grid(
    row=5,
    column=0,
    padx=5,
    pady=3,
    ipadx=3,
    ipady=3
)

# BarProgress
progress_bar = ttk.Progressbar(
    window,
    orient="horizontal",
    length=300,
    mode="determinate"
)

progress_bar.grid(
    row=6
)

progress_label = Label(
    window,
    text=""
)

progress_label.grid(
    row=7
)

# Button exit
btn_exit = Button(
    window,
    text='Sair',
    command=window.quit
)

btn_exit.grid()

# Start screen
window.mainloop()
