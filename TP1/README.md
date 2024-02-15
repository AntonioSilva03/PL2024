<h1 align="center"> TPC1</h1>

## Autor:
- António Filipe Castro Silva
- A100533

## Objetivo:

O objetivo deste TPC é, a partir de um ficheiro CSV disponibilizado pelos professores com informações acerca de 300 atletas, sem utilizar o módulo CSV, obter os seguintes dados:
- Lista ordenada alfabeticamente das modalidades desportivas
- Percentagens de atletas aptos e inaptos para a prática desportiva
- Distribuição de atletas por escalão etário (escalão = intervalo de 5 anos)

## Resolução:

Para resolver este TPC, formulei a resolução em 4 partes:

- Inicialmente, trato de ler o CSV e colocar os dados todos processados num array e depois crio o ficheiro ([resultados.txt](https://github.com/AntonioSilva03/PL2024/blob/main/TP1/resultados.txt)) onde irei escrever os resultados requisitados.
- A primeira query pede para ordenar as modalidades, logo comecei por colocar num array todas as modalidades existentes, somente na primeira vez que apareciam num
dado atleta, depois ordenei-as alfabeticamente e, por fim, escrevias no ficheiro enumeradamente.
- A segunda query pede a percentagem de atletas aptos e inaptos, logo primeiro calculei quantos havia de cada e depois calculei as percentagens. Depois dos cálculos escrevi no ficheiro o número de atletas aptos e inaptos e as suas percentagens correspondentes.
- Por fim, na terceira query, comecei por calcular a maior idade e a menor idade entre os atletas, para escolher da melhor forma os intervalos dos escalões. Seguidamente, coloquei cada atleta no seu respetivo escalão e ordenei o escalão por idade e seguidamente por ordem alfabética. Finalmente escrevi no ficheiro o nome dos atletas que estão em cada escalão, tal como o número de atletas e a sua percentagem por escalão.

Para finalizar fechei o ficheiro de resultados para melhor organização.
