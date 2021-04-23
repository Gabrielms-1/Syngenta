Processo Seletivo Syngenta Digital

# Etapa 1:

Usando a biblioteca de imagens do Python (PIL) foi possível transformar cada pixel da imagem em um vetor, adicionar a uma lista e assim identificar os valores RGB de cada um.
Com isso, bastou apenas contar quantas vezes cada vetor de pixel se repete durante toda a imagem.
Bastou apenas fixar os valores RGB do preto (0, 0, 0) e do branco (255, 255, 255) que podem ser explicitamente vistos na imagem. Como há apenas 3 cores,
os pixels restantes seriam obrigatoriamente verdes, resultando assim num total de **298 pixels verdes**

><p>As cores encontradas foram:  [(0, 0, 0), (96, 192, 0), (255, 255, 255)]</p>
><p>Quantidade de pixels verde:  298</p>
><p>Quantidade de pixels preto:  125236</p>
><p>Quantidade de pixels branco:  466</p>


Também resolvi utilizar a biblioteca **Numpy** para confirmar o cálculo usando uma segunda metodologia.
Para isso, bastou apenas converter a imagem num Array do Numpy, retornando um Array com todos os valores RGB presentes em toda a imagem.
Com isso bastou apenas a manipulação desse array, transformando-o em uma matriz de ordem _ix3_ (quantidade de linhas desconhecida x 3 colunas) e removendo os arrays duplicados.
Tendo os valores de pixels únicos em uma matriz, bastou apenas definir quais posições seriam correspondentes a cada cor e imprimir esse valores.
><p>Preto  =  [0 0 0]</p>
><p>Verde  =  [ 96 192   0]</p>
><p>Branco =  [255 255 255]</p>
><p>Quantidade de pixels pretos:   125236</p>
><p>Quantidade de pixels verdes:   298</p>
><p>Quantidade de pixels brancos:  466</p>

# Etapa 2:
Para a segunda etapa, usei 3 métodos diferentes.

### Método 1: Análise de bytes (Sem sucesso)
Nesse método, converti a imagem num vetor de bytes, em seguida converti em uma lista e converti cada valor em char.

### Método 2: Edge Detection usando OpenCV e Matplotlib (Sem sucesso)
Nesse método tentei utilizar método de detecção de bordas do OpenCV para ver as bordas formavam alguma imagem e a biblioteca Matplotlib para gerar as imagens modificadas na tela.
Foram utilizados o método LaPlace e Sobel no eixo X e no eixo Y.

### Método 3: Separação de canais de cores (Sem sucesso)
Nesse método tentei separar os 3 canais de cores (Vermelho, Verde e Azul) usando Numpy em criando 3 novas imagens distintas usando OpenCV para ver se revelava alguma informação em apenas 1 canal de cor. (Imagens na pasta da Etapa 2)
