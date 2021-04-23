
image = open('Syngenta.bmp', 'rb')
data = image.read()

mask =  0b01111111
ascii_list = []
string = ""

for x in data:
    value = mask & x
    ascii_list.append(value)

for y in ascii_list:
    string = string + chr(y)

print(string)