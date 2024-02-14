import os

#Leitura e Processamento do CSV

with open("emd.csv", "r", encoding='utf-8') as emd:
    dados = emd.read()

dados_array = []

for linha in dados.split("\n")[1:]:
    linha_processada = linha.split(",")
    dados_array.append(linha_processada)

resultados = open("resultados.txt", "w", encoding="utf-8")

#Modalidades

modalidades = []

for linha in dados_array:
    modalidade = linha[8]
    if modalidade not in modalidades:
        modalidades.append(modalidade)
modalidades.sort()
resultados.write("Lista ordenada alfabeticamente das modalidades desportivas: " + "\n")
i = 1
for modalidade in modalidades:
    resultados.write(str(i) + ". " + modalidade + "\n")
    i = i + 1
resultados.write("\n")

#Atletas aptos e inaptos
    
atletas = len(dados_array)
aptos = 0
inaptos = 0
for linha in dados_array:
    if linha[12] == "true":
        aptos += 1
    else:
        inaptos += 1

percentagem_aptos = (aptos / atletas) * 100
percentagem_inaptos = 100 - percentagem_aptos
aptos_arredondar = round(percentagem_aptos, 2)
inaptos_arredondar = round(percentagem_inaptos, 2)

resultados.write("Percentagens de atletas aptos e inaptos para a prática desportiva: " + "\n")
resultados.write("Atletas aptos: " + str(aptos) + " alunos-> " + str(aptos_arredondar) + "%" + "\n")
resultados.write("Atletas inaptos: " + str(inaptos) + " alunos-> " + str(inaptos_arredondar) + "%" + "\n\n")

#Escalão Etário

escaloes = {}
min_idade = 100
max_idade = 0

for linha in dados_array:
    idade = int(linha[5])
    if idade > max_idade:
        max_idade = idade
    if idade < min_idade:
        min_idade = idade

i = min_idade
while i <= max_idade:
    escalao = str(i) + "-" + str(i+ 4)
    escaloes[escalao] = None
    i = i + 5

for linha in dados_array:
    idade = int(linha[5])
    nome = linha[3] + " " + linha[4] + ", Idade: " + linha[5]
    for escalao,_ in escaloes.items():
        min_idade, max_idade = map(int, escalao.split("-"))
        if min_idade<=idade<=max_idade:
            if escaloes[escalao] is None:
                escaloes[escalao] = [nome]
            else:
                escaloes[escalao].append(nome)

resultados.write("Distribuição de atletas por escalão etário (escalão = intervalo de 5 anos): \n")
for escalao, atletas in escaloes.items():
    resultados.write("Escalão " + escalao +": " + str(atletas) + "\n")

resultados.close()       