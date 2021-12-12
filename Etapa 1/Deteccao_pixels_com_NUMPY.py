from PIL import Image
import numpy as np

# Abre a imagem e converte para garantir que esteja em RGB
im = Image.open('Syngenta.bmp').convert('RGB')

# Converte para um array do Numpy
imageArray = np.array(im)
#print(imageArray)

# Organiza todos os pixels em matrizes [ix4] (x linhas e 3 colunas) e remove os valores duplicados
colors, counts = np.unique(imageArray.reshape(-1,3), axis=0, return_counts=1)

print("Preto  = ", colors[0])
print("Verde  = ", colors[1])
print("Branco = ", colors[2])

print("Quantidade de pixels pretos:  " , counts[0])
print("Quantidade de pixels verdes:  " , counts[1])
print("Quantidade de pixels brancos: " , counts[2])
