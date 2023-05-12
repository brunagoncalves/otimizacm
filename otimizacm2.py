from tkinter import *
from tkinter import font

# Create window tkinter
window = Tk()
window.title('OtimizaCM')
window.iconphoto(True, PhotoImage(file='./icons/icon-app.png'))

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

# Select folders
label_folder_image = Label(window, text='Selecione a pasta das imagens para Redimensionar ou Renomear.', bg='#fff18c')
label_folder_image.grid(row=0, columnspan=4, **padding, **ipadding, sticky=NSEW)

btn_folder_image = Button(window, image=icon_folder)
btn_folder_image.grid(row=1, column=0, **padding, **ipadding, sticky=NSEW)

label_path_image = Label(window, text='caminho pegar', bg='#fff18c')
label_path_image.grid(row=1, columnspan=3, **padding, **ipadding, sticky=NE)

# label_folder_save = Label(window, text='Selecione a pasta onde quer salvar.', bg='#fff18c')
# label_folder_save.grid(row=2, columnspan=4, **padding, **ipadding, sticky=EW)

# btn_folder_save = Button(window, image=icon_folder)
# btn_folder_save.grid(row=3, column=0, **padding, **ipadding, sticky=NW)

# label_path_save = Label(window, text='caminho salvar', bg='#fff18c')
# label_path_save.grid(row=3, columnspan=3, **padding, **ipadding, sticky=NSEW)

# btn_resize_report = Button(window, text='Redimensionar Relatórios')
# btn_resize_report.grid(row=4, column=1, **padding, **ipadding)

# btn_resize_ipad = Button(window, text='Redimensionar Ipad')
# btn_resize_ipad.grid(row=4, column=2, **padding, **ipadding)

# btn_rename_report = Button(window, text='Renomear para Relatórios')
# btn_rename_report.grid(row=4, column=3, **padding, **ipadding)

label_author = Label(window, text='Desenvolvido por Bruna Gonçalves', bg='#fff18c')
label_author.grid(row=5, columnspan=4, **padding, **ipadding, sticky=EW)

# Start screen
window.mainloop()
