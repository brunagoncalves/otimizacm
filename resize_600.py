import os
from PIL import Image

# Define o tamanho da imagem redimensionada...
new_size = (600, 600)

# Diretório das imagens que serão redimensionadas...
folder_todo = '../otimiza-fotos/to-do'

# Diretório das imagens já redimensionadas...
folder_done = '../otimiza-fotos/done'

# Percorra por cada imagem a ser redimensionada...
for image in os.listdir(folder_todo):
    # Verifique se o arquivo é uma imagem
    if image.endswith(".jpg") or image.endswith(".png"):
        # Abra a imagem original
        path_todo = os.path.join(folder_todo, image)
        imagem_todo = Image.open(path_todo)

        # Redimensione a imagem
        resize_image = imagem_todo.resize(new_size)

        # Especifique o caminho para salvar a imagem redimensionada
        resize_path = os.path.join(folder_done, image)

        # Salve a imagem redimensionada em um novo arquivo
        resize_image.save(resize_path)
