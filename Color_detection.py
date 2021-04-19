import PIL
from PIL import Image
import os

# TEST ON PC
os.chdir(r'/home/ddp/Desktop/Syngenta/')
print(os.getcwd())

img = PIL.Image.open("Syngenta.bmp")    # Abre a imagem
rgb_im = img.convert('RGB')             # Garante que a imagem esteja em RGB

width, length = rgb_im.size             # Define o tamanho da imagem em Largura x Altura

pixelValues = []                        # Cria uma lista onde serão armazenados os valores RGB de cada pixel

for col in range(width):                        # Loop para a adiçao de cada pixel a lista
    for row in range(length):
        pixels = rgb_im.getpixel((col, row))
        pixelValues.append(pixels)

uniquePixels = list(dict.fromkeys(pixelValues))  # Remove os valores de cores duplicados

#print(uniquePixels)

black = 0
white = 0
green = 0

for item in pixelValues:            # Loop para contagem das cores
    if(item == (0, 0, 0)):          # Valor RGB para PRETO
        black += 1
    elif(item == (255, 255, 255)):  # Valor RGB para BRANCO
        white += 1
    else:                           # Como a imagem possui 3 cores, se não for branco e nem preto, será verde
        green += 1

print(green)

