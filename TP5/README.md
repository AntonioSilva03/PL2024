# TPC5: Máquina de Vending

## Autor:
- António Filipe Castro Silva
- A100533

## Objetivo:

Construir um programa que simule uma máquina de vending que responde a vários pedidos.

## Resumo:

Na main começa-se por ver a data do dia atual, inicializar o lexer, alguns dos seus dados e abrir o json file onde temos a stock da vending machine.

A partir daí a máquina fica à espera das várias operações que estão programadas:

- LISTAR: Mostra todos os artigos que estão em stock, mostrando o seu código, nome, quantidade e preço.

- MOEDA: Introdução de moedas na máquina para aumentar o saldo do utilizador. Só aceita moedas de 2€, 1€, 50c, 20c, 10c, 5c, 2c e 1c. Após introdução das moedas, mostra o saldo final. Cada moeda tem de ser separada por uma vírgula, senão só acrescenta o primeiro valor.

- SELECIONAR: Selecionar um artigo que se queira da máquina a partir do seu código. Se não houver problemas, paga-se o produto, recebe-se e visualizamos o novo saldo. Caso o produto esteja esgotado, somos informados acerca disso. Caso não tenhamos saldo suficiente, somos informados do nosso saldo e do valor do produto. O último caso é o código desse produto nem existir.

- SALDO: Aparece no ecrã o nosso saldo atual. Em todas as informações de saldo, caso uma pessoa tenha menos de 1€, só aparecem os cêntimos.

- ADICIONAR: Adição de produtos em stock. Caso o produto que queremos acrescentar exista, simplesmente aumenta a sua quantidade em stock, senão temos de informar o nome e o preço do novo produto a acrescentar. Qualquer operação que possa causar alterações no dataset, atualiza imediatamente, tendo no final da main uma atualização final, caso algo tenha escapado.

- SAIR: Quando um utilizador quer sair da máquina, este recebe o troco das moedas que colocou na máquina, sendo as moedas que vão ser entregues calculadas na operação em si. Caso não haja troco, o utilizador é informado acerca disso

Para correr este programa basta correr no terminal: `python vending.py db.json`