import sys

bits_deslocamento = 12  #tamanho do deslocamento; 4kb, logo 2^12
tamanho_pagina = 2**bits_deslocamento  # tamanho da pagina

def calcular_pagina_deslocamento(endereco):

    numero_pagina = endereco >> bits_deslocamento #pega endereco e desloca 12 bits para a direita, o equivalente a dividir o endereco por 2 na 12 bits de deslocamento ou 4096
    deslocamento = endereco & (tamanho_pagina - 1) #mascara de bits para manter os bits importantes que vao ser usados, os irrelevantes vao embora
    return numero_pagina, deslocamento 

endereco = int(sys.argv[1])

if (endereco < 0) or (endereco > 0b1111111111111111):
    print("Endereço de 16 bits inválido")
    sys.exit()

numero_pagina, deslocamento = calcular_pagina_deslocamento(endereco) #pegando os valores em sequencia la da funcao 

endereco_virtual = numero_pagina * (2**bits_deslocamento ) + deslocamento

with open('data_memory.txt', 'r') as f:
    for i in range(endereco_virtual):  #pra percorrer até o valor colocado
        valor_pos = int(f.readline().strip())

print(f'numero da pagina = {numero_pagina}')
print(f'deslocamento = {deslocamento}')
print(f'valor da posicao: {valor_pos}')
print(f'valor do endereço virtual: {endereco_virtual} ')
