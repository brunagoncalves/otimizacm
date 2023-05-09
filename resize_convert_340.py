import os
from PIL import Image

# Define o novo tamanho da imagem...
new_size = (340, 340)

# Diretório das imagens originais...
folder_todo = '../otimiza-fotos/to-do'

# Diretório das imagens redimensionadas...
folder_done = '../otimiza-fotos/done'

# Percorra por cada imagem no diretório original...
for image in os.listdir(folder_todo):
    # Verifique se o arquivo é uma imagem PNG
    if image.endswith(".png"):
        # Abre a imagem original
        path_todo = os.path.join(folder_todo, image)
        image_origin = Image.open(path_todo)

        # Redimensiona a imagem
        image_resize = image_origin.resize(new_size)

        # Salvar imagem no diretório de imagens redimensionadas
        image_jpg = os.path.splitext(image)[0] + ".jpg"
        path_resize = os.path.join(
            folder_done, image_jpg)

        # Salvar a imagem redimensionada em um novo arquivo JPG
        image_resize.convert('RGB').save(path_resize)

    # Se o arquivo for uma imagem JPG, apenas redimensione e salve
    elif image.endswith(".jpg"):
        # Abra a imagem original
        path_todo = os.path.join(folder_todo, image)
        image_origin = Image.open(path_todo)

        # Redimensione a imagem
        image_resize = image_origin.resize(new_size)

        # Salvar imagem no diretório de imagens redimensionadas
        path_resize = os.path.join(folder_done, image)

        # Salvar a imagem redimensionada em um novo arquivo JPG
        image_resize.save(path_resize)
