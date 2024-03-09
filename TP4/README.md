# TPC4:

## Autor:
- António Filipe Castro Silva
- A100533

## Objetivo:

Construir um analisador léxico para uma linguagem de query.

## Resumo:

- Este programa utiliza a biblioteca PLY (Python Lex-Yacc) que utiliza um analisador léxico para comandos SQL básicos.
- Começamos por definir os tokens e as expressões regulares para cada um deles, também definimos uma função de caso de erro
- Na main recebe como input o ficheiro que quer analisar e depois escreve a resposta, depois da sua análise léxica, no ficheiro de output

Exemplo: `python analex.py ./input.txt ./output.txt`