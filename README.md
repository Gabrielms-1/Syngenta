Processo Seletivo Syngenta Digital

# Etapa 1:

Usando Python puro foi possível transformar cada pixel da imagem em um vetor, adicionar a uma lista e assim identificar os valores RGB de cada um.
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

