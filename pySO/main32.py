import sys

bits_deslocamento = 12  #tamanho do deslocamento
bits_pagina = 10
mascara_deslocamento = 2**bits_deslocamento - 1 # tamanho do deslocamento

def calcular_paginas_deslocamento(endereco):

    numero_pagina1 = endereco >> (bits_deslocamento + bits_pagina) #pega endereco e desloca 12 bits main 10 da página para a direita, o equivalente a dividir o endereco por 2 na 12 bits de deslocamento ou 4096
    numero_pagina2 = (endereco >> bits_deslocamento) & 0x3ff
    deslocamento = endereco & mascara_deslocamento #mascara de bits para manter os bits importantes que vao ser usados, os irrelevantes vao embora
    return numero_pagina1, numero_pagina2, deslocamento

endereco = int(sys.argv[1])

numero_pagina1, numero_pagina2, deslocamento = calcular_paginas_deslocamento(endereco) #pegando os valores em sequencia la da funcao 

endereco_fisico = (numero_pagina1 * (2**bits_deslocamento)) + (numero_pagina2 * (2**bits_deslocamento)) + deslocamento

with open('data_memory.txt', 'r') as f:
    for i in range(endereco_fisico):  #pra percorrer até o valor colocado
        valor_pos = int(f.readline())

print(f'numero da pagina 1 = {numero_pagina1}')
print(f'numero da pagina 2 = {numero_pagina2}')
print(f'deslocamento = {deslocamento}')
print(f'valor da posicao: {valor_pos} ')
print(f'valor do endereço físico: {endereco_fisico} ')