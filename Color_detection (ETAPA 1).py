import PIL
from PIL import Image

img = PIL.Image.open("Syngenta.bmp")    # Abre a imagem
rgb_im = img.convert('RGB')             # Garante que a imagem esteja em RGB

width, length = rgb_im.size             # Define o tamanho da imagem em Largura x Altura

pixelValues = []                        # Cria uma lista onde serão armazenados os valores RGB de cada pixel

for col in range(width):                        # Loop para a adiçao de cada pixel à lista
    for row in range(length):
        pixels = rgb_im.getpixel((col, row))
        pixelValues.append(pixels)

uniquePixels = list(dict.fromkeys(pixelValues))  # Remove os valores de cores duplicados

print("As cores encontradas foram: " , uniquePixels)

black = 0
white = 0
green = 0

for item in pixelValues:            # Loop para contagem das cores
    if(item == (0, 0, 0)):          # Valor RGB para PRETO (cor visivelmente mais presente na imagem e com valores RGB conhecidos: R = 0, G = 0, B = 0)
        black += 1
    elif(item == (255, 255, 255)):  # Valor RGB para BRANCO (segunda cor com valores RGB conhecidos na imagem: R = 255, G = 255, B = 255)
        white += 1
    else:                           # Como a imagem possui 3 cores, se não for branco (255, 255, 255) e nem preto (0, 0, 0), será verde
        green += 1

print("Quantidade de pixels verde: ", green)
print("Quantidade de pixels preto: ", black)
print("Quantidade de pixels branco: ", white)


