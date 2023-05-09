import os

# def rename_files():
# Diretório que contém os arquivos para renomear...
path = '../otimiza-fotos/rename'

# Percorrer todos os arquivos no diretório e verifica a contagem dos caracteres...
for filename in os.listdir(path):
    if len(filename) == 16:
        new_name = filename[:10] + filename[12:]
    elif len(filename) == 17:
        new_name = filename[:11] + filename[13:]
    elif len(filename) == 18:
        new_name = filename[:12] + filename[14:]
    else:
        continue
    # Renomeia os arquivos...
    os.rename(os.path.join(path, filename), os.path.join(path, new_name))
