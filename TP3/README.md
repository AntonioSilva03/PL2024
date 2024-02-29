# TPC3:

## Autor:
- António Filipe Castro Silva
- A100533

## Objetivo:

O objetivo deste TPC é correr um ficheiro que some todas as sequências de dígitos que encontre, tendo em conta vários casos especiais.

## Resumo:

Para resolver este TPC começa-se por criar um regex que vai tratar de todos os casos:

- Caso sejam números ficam guardados no group 'sum'
- Caso encontre um "on" fica guardado no group 'on', tendo este em conta todos os casos de maísculas e minúsculas
- Caso encontre um "off" fica guardado no group 'off', tendo em conta os mesmos casos que o 'on'
- Caso encontre um "=", fica guardado no group 'show'

Este regex serve para, na main em si, depois de aberto o ficheiro de [teste](https://github.com/AntonioSilva03/PL2024/tree/main/TP3/test.txt) e sendo este lido linha à linha:
- se encontrar algo do group 'sum', adiciona à variável "soma" que vai guardando todos os valores encontrados, quando o state é True
- se encontrar algo do group 'on', altera o state para True caso este esteja False, senão continua igual
- se encontrar algo do group 'off', altera o state para False caso esteja True, senão continua igual
- se encontrar algo do group 'show', apresenta na consola o valor da variável "soma" atualmente.

Para correr o programa basta fazer deste modo: `python programa.py <caminho_para_arquivo>`.
O programa inicia com o state a False, ou seja, só começa a somar depois de encontrar o primeiro 'on' e obviamente a soma inicia-se a 0.
