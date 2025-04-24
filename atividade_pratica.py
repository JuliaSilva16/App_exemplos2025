#Etapa 1 - Criar uma lista com os nomes de 5 objetos
objetos = ['garrafa', 'copo', 'prato', 'talher', 'taça']
print('lista de objetos criada:',objetos)

#Etapa 2 - Adicione mais um onjeto ao finla da lista
objetos.append('colher')
print('Objeto adicionado',objetos)

#Etapa 3 - Acesse o objeto que está na 2° posição
varificacao = objetos[2]
print('Acessado com sucesso:',varificacao)

#Etapa 4  - Remova um objeto da lista
objetos.remove('garrafa')
print("Objeto removido")

#Etapa 5 - Exiba o tamanho da lista
len(objetos)
print('A lista tem :',len(objetos))

#Etapa 6 - Mostre todos os itens com um laço for
for objeto in objetos:
    print(objeto)

#Etapa 7 - Verifique se 'cadeira' está na lista.Se sim remova-a,se não adicione
verificar = 'cadeira' in objetos
if 'cadeira' in objetos:
    objetos.remove('cadeira')
    print('Objeto removido')
    print(len(objetos))
else:
    objetos.append('cadeira')
    print("Objeto adicionado")
    print(objetos)

#Etapa 8 - Ordene a lista em ordem alfabética    ]
objetos.sort()
print('Lista em ordem alfabética:',objetos)

#Etapa 9 - Exiba o primeiro e o último objeto
ordem_um = objetos[1]
print('primeiro objeto:', ordem_um)

oredem_ultimo = objetos[len(objetos)-1]
print('ultimo objeto:', oredem_ultimo)

#Etapa 10 - Limpe toda a lista
objetos.clear()
print('lista limpa:')
print(objetos)




