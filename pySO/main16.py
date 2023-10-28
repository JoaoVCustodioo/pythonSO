import sys

bits_deslocamento = 12  #tamanho do deslocamento 
tamanho_pagina = 2**bits_deslocamento  # tamanho da pagina

def calcular_pagina_deslocamento(endereco):

    numero_pagina = endereco >> bits_deslocamento #pega endereco e desloca 12 bits para a direita, o equivalente a dividir o endereco por 2 na 12 bits de deslocamento ou 4096
    deslocamento = endereco & (tamanho_pagina - 1) #mascara de bits para manter os bits importantes que vao ser usados, os irrelevantes vao embora
    return numero_pagina, deslocamento 

endereco = int(sys.argv[1])

numero_pagina, deslocamento = calcular_pagina_deslocamento(endereco) #pegando os valores em sequencia la da funcao 

endereco_fisico = numero_pagina * (2**bits_deslocamento ) + deslocamento

with open('data_memory.txt', 'r') as f:
    for i in range(endereco_fisico):  #pra percorrer até o valor colocado
        valor_pos = int(f.readline().strip())

print(f'numero da pagina = {numero_pagina}')
print(f'deslocamento = {deslocamento}')
print(f'valor da posicao: {valor_pos}')
