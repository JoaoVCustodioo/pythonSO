import sys

bits_deslocamento = 12  #tamanho do deslocamento 
tamanho_pagina = 2**bits_deslocamento  # tamanho da pagina

def calcular_pagina_deslocamento(endereco):
   
    numero_pagina = endereco >> bits_deslocamento #pega endereco e desloca 12 bits para a direita
    deslocamento = endereco & (tamanho_pagina - 1) #mascara de bits para manter os bits importantes que vao ser usados
    return numero_pagina, deslocamento 

def ler_endereco_arquivo(nome_arquivo):
        with open(nome_arquivo, 'r') as f:
            endereco = int(f.readline().strip())
            return endereco
    
    
if len(sys.argv) > 1:
    if sys.argv[1].isdigit():
        endereco = int(sys.argv[1])
    else:
        endereco = ler_endereco_arquivo(sys.argv[1])


numero_pagina, deslocamento = calcular_pagina_deslocamento(endereco) #pegando os valores em sequencia la da funcao 

with open('data_memory.txt', 'r') as f:
    for i in range(endereco + 1):  #pra percorrer até o valor colcado
        valor_pos = int(f.readline().strip())


print(f'numero da pagina = {numero_pagina}')  
print(f'deslocamento = {deslocamento}')  
print(f'valor da posicao: {valor_pos} ')
