# TPC2:

## Autor:
- António Filipe Castro Silva
- A100533

## Objetivo:

O objetivo deste TPC é, a partir de um ficheiro MD que eu criei com exemplo, converté-lo para um ficheiro HTML com o mesmo conteúdo, alterando para o contexto da linguagem HTML.

## Resolução:

Para resolver este TPC formulei a resolução em 3 partes:

- Primeiro começo por meter nos argumentos da execução o ficheiro md que quero converter, leio-o e crio o ficheiro html com o mesmo nome mas sufixo diferente e começo por escrever nele o ficheiro md inicial.

- Passada esta leitura e escrita, chamo a função conversor que realmente tratará de converter o ficheiro md para html. Tratamos de todos os diferentes casos: cabeçalhos, negritos, itálico, blockquotes, listas ordenadas, blocos de código, horizontal rule, imagens e por fim links.

- Para finalizar criamos uma fstring onde iremos inicializar o ficheiro html, colocar todo o conteúdo md já convertido e fechamos essa string onde está o ficheiro html e enviamos para a main que tratará então de criar o novo ficheiro html que já tem todo o ficheiro convertido.

## Ficheiros:

[Ficheiro teste md](https://github.com/AntonioSilva03/PL2024/tree/main/TP2/example.md)

[Ficheiro convertido para html](https://github.com/AntonioSilva03/PL2024/tree/main/TP2/example.html)