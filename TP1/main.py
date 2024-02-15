import os

#Leitura e Processamento do CSV

with open("emd.csv", "r", encoding='utf-8') as emd:
    dados = emd.read()

dados_array = []

for linha in dados.split("\n")[1:]:
    linha_processada = linha.split(",")
    dados_array.append(linha_processada)

#Criação do ficheiro onde escreverei os resultados

resultados = open("resultados.txt", "w", encoding="utf-8")

#Modalidades

modalidades = []

#Colocar todas as modalidades existentes num array
for linha in dados_array:
    modalidade = linha[8]
    if modalidade not in modalidades:
        modalidades.append(modalidade)
modalidades.sort() #Organizar alfabeticamente
resultados.write("Lista ordenada alfabeticamente das modalidades desportivas: " + "\n\n")
i = 1
for modalidade in modalidades:
    resultados.write(str(i) + ". " + modalidade + "\n") #Escrita no ficheiro
    i = i + 1

resultados.write("__________________________________________________________________\n")

#Atletas aptos e inaptos
    
atletas = len(dados_array)
aptos = 0
inaptos = 0
#Cálculo do número de aptos e inaptos
for linha in dados_array:
    if linha[12] == "true":
        aptos += 1
    else:
        inaptos += 1

#Cálculo das percentagens e arredondamentos
percentagem_aptos = (aptos / atletas) * 100
percentagem_inaptos = 100 - percentagem_aptos
aptos_arredondar = round(percentagem_aptos, 2)
inaptos_arredondar = round(percentagem_inaptos, 2)

#Escrita no ficheiro
resultados.write("Percentagens de atletas aptos e inaptos para a prática desportiva: " + "\n\n")
resultados.write("Atletas aptos: " + str(aptos) + " alunos-> " + str(aptos_arredondar) + "%" + "\n")
resultados.write("Atletas inaptos: " + str(inaptos) + " alunos-> " + str(inaptos_arredondar) + "%" + "\n")

resultados.write("___________________________________________________________________________\n")

#Escalão Etário

escaloes = {}
min_idade = 1000
max_idade = -1

#Cálculo da menor e maior idade
for linha in dados_array:
    idade = int(linha[5])
    if idade > max_idade:
        max_idade = idade
    if idade < min_idade:
        min_idade = idade

#Organização dos escalões
i = min_idade
while i <= max_idade:
    escalao = str(i) + "-" + str(i+ 4)
    escaloes[escalao] = None
    i = i + 5

#Colocação de cada atleta no seu escalão etário
for linha in dados_array:
    idade = int(linha[5])
    nome = linha[3] + " " + linha[4] + ", Idade: " + linha[5]
    for escalao,_ in escaloes.items():
        min_idade, max_idade = map(int, escalao.split("-"))
        if min_idade<=idade<=max_idade:
            if escaloes[escalao] is None:
                escaloes[escalao] = [(nome,idade)]
            else:
                escaloes[escalao].append((nome,idade))

#Sort dos atletas dentro do seu escalao primeiro pela idade e depois pelo nome
for escalao, atletas in escaloes.items():
    escaloes[escalao] = sorted(atletas, key=lambda x: (x[1], x[0]))

#Escrita no ficheiro
resultados.write("Distribuição de atletas por escalão etário (escalão = intervalo de 5 anos): \n\n")
for escalao, atletas in escaloes.items():
    num_atletas = len(dados_array)
    atletas_escalao = len(atletas)
    last_escalao = list(escaloes.keys())[-1]
    percentagem_escalao = (atletas_escalao / num_atletas) * 100
    resultado_escalao = "\n".join([atleta[0] for atleta in atletas])
    if escalao != last_escalao:
        resultados.write(f"Escalão {escalao} ({atletas_escalao } atletas, {percentagem_escalao:.2f}%):\n\n{resultado_escalao}\n\n")
    else:
        resultados.write(f"Escalão {escalao} ({atletas_escalao } atletas, {percentagem_escalao:.2f}%):\n\n{resultado_escalao}")

resultados.close()       