# Python Lista 3
# Aluno: Vitor Daniel Vieira de Queiroz

# 1) Implementar um programa que receba um nome de arquivo e gere estatísticas sobre o
# arquivo (número de caracteres, número de linhas e número de palavras)

# caracters = palavras = linhas = 0
# listaPalavras = []
# with open('arquivo.txt', 'r') as arquivo:
# 	for linha in arquivo:
# 		linhas += 1
# 		listaPalavras.append(linha.split())

# for palavra in listaPalavras:
# 	for caracter in palavra:
# 		caracters += len(caracter)

# print('Numero de Caracters: ' + str(caracters))
# print('Numero de Linhas: ' + str(linhas))
# print('Numero de Palavras: ' + str(len(listaPalavras)))


# 2) Faça um script que:
# ▪ Leia um arquivo texto.
# ▪ Conte as ocorrências de cada palavra.
# ▪ Mostre os resultados ordenados pelo número de ocorrências


# listaPalavras = []
# with open('arquivo.txt', 'r') as arquivo:
# 	for linha in arquivo:
# 		listaPalavras.append(linha.split())

# palavras = []
# for lista in listaPalavras:
#     for elemento in lista:
#         palavras.append(elemento)

# ocorrencias = {}
# for palavra in palavras:
# 	ocorrencias.update({palavra : palavras.count(palavra)})

# print(palavras)
# print(ocorrencias)

# ocorrenciasOrdenadas = sorted(ocorrencias.items(), key = lambda t:t[1]) #Ordendo por Valores
# print('Lista de Ocorrencias ordenadas: ' + str(ocorrenciasOrdenadas))

# 3) Terceira Questao
def hbytes(num):
    for x in ['bytes','KB','MB','GB']:
        if num < 1024.0:
            return "%1.3f %s" % (num, x)
        num /= 1024.0
    return "%1.3f %s " % (num, 'TB')

listaUsuarios = []
# Total de Espaço Consumido 2581,56Mb ou 2706979865 bytes
cont = 0
total = 0
pct = 0
with open('usuarios.txt', 'r') as arquivo:
	for linha in arquivo:
		listaUsuarios.append(linha.split())

	for usuario in listaUsuarios:
		cont += 1
		usuario.insert(0,cont) #inserir no começo da lista
		usuario.append(hbytes(int(usuario[2])))
		total += int(usuario[2])

	for usuario in listaUsuarios:
		usuario.append(float(usuario[2])/(total))
		usuario.append("{:.2%}".format(usuario[4]))

print(listaUsuarios)
print(hbytes(total))
numTotal = hbytes(total).split(' ')
media = float(numTotal[0])/cont*1000
print(hbytes(total).split(' '))
print(str(media) + ' MB')


with open('relatorio.txt', 'w') as relatorio:
	relatorio.write('ACME Inc.                                             Uso do Espaço em disco pelos usuários\n¡½')
	relatorio.write('-------------------------------------------------------------------------------------------')	



