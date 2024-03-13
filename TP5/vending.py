import json
import re
import sys
from ply import lex
from datetime import date

argv = None

tokens = [
    'LISTAR',
    'MOEDA',
    'SELECIONAR',
    'SALDO',
    'ADICIONAR',
    'SAIR',
]

def t_LISTAR(t):
    r'LISTAR'
    print("""maq:
cod | nome | quantidade |  preço
------------------------------------""")
    for produto in t.lexer.data['stock']:
        print(f"{produto['cod']} | {produto['nome']} | {produto['quantidade']} | Preço: {produto['preco']}\n")
    return t


def t_MOEDA(t):
    r'MOEDA\s((2e|1e|50c|20c|10c|5c|2c|1c)(?:\s*,\s*(2e|1e|50c|20c|10c|5c|2c|1c))*)'  
    matches = re.findall(r'(2e|1e|50c|20c|10c|5c|2c|1c)', t.value)  
    for match in matches:
        value = re.findall(r'\d{1,2}', match)[0]
        currency = match[-1]  # Extract the currency symbol
        if currency == 'c':
            t.lexer.saldo += round(int(value) / 100,2)
        else:
            t.lexer.saldo += round(float(value),2)
    euros = round(int(t.lexer.saldo),2)
    cents = round(int((t.lexer.saldo - euros) * 100),2)
    print(f"maq: Saldo = {euros}e{cents}c")
    return t

def t_SELECIONAR(t):
    r'SELECIONAR\s\w+'
    produto_cod = t.value.split()[1]
    for produto in t.lexer.data['stock']:
        if produto['cod'] == produto_cod:
            if t.lexer.saldo >= produto['preco'] and produto['quantidade'] > 0:
                t.lexer.saldo -= produto['preco']
                produto['quantidade'] -= 1
                print(f'maq: Pode retirar o produto dispensado "{produto["nome"]}"')
                with open(argv[1], "w", encoding="utf-8") as file:
                    json.dump(t.lexer.data, file, indent=2, ensure_ascii=False)
                euros = round(int(t.lexer.saldo),2)
                cents = round(int((t.lexer.saldo - euros) * 100),2)
                if(euros == 0):
                    print(f"maq: Saldo: {cents}c")
                else: 
                    print(f"maq: Saldo: {euros}e{cents}c")
            elif produto['quantidade'] <= 0:
                print(f"Desculpe, o Produto {produto['nome']} está esgotado")
            else:
                print(f"maq: Saldo insuficiente para satisfazer o seu pedido")
                euros = round(int(t.lexer.saldo),2)
                cents = round(int((t.lexer.saldo - euros) * 100),2)
                produto_euros = round(int(produto['preco']),2)
                produto_cents = round(int((produto['preco'] - produto_euros) * 100),2)
                if(euros == 0 and produto_euros != 0):
                    print(f"maq: Saldo = {cents}c; Pedido = {produto_euros}e{produto_cents}c ")
                if(produto_euros == 0 and euros != 0):
                    print(f"maq: Saldo = {euros}e{cents}c; Pedido = {produto_cents}c ")
                if(euros == 0 and produto_euros == 0):
                    print(f"maq: Saldo = {cents}c; Pedido = {produto_cents}c ")
                else:
                    print(f"maq: Saldo = {euros}e{cents}c; Pedido = {produto_euros}e{produto_cents}c ")
            return t
    
    print(f"Produto {produto_cod} não existe")
    return t

def t_SALDO(t):
    r'SALDO'
    euros = round(int(t.lexer.saldo),2)
    cents = round(int((t.lexer.saldo - euros) * 100),2)
    if(euros == 0):
        print(f"maq: Saldo: {cents}c")
    else: 
        print(f"maq: Saldo: {euros}e{cents}c")
    return t

def t_ADICIONAR(t):
    r'ADICIONAR\s\w+\s\d+'
    produto_cod = t.value.split()[1]
    quantidade = int(t.value.split()[2])
    for produto in t.lexer.data['stock']:
        if produto['cod']==produto_cod:
            produto['quantidade'] += quantidade
            if quantidade == 1:
                print(f"{quantidade} unidade do {produto_cod} foi  adicionada com sucesso")
            else:
                print(f"{quantidade} unidades do {produto_cod} foram  adicionadas com sucesso")
            with open(argv[1], "w", encoding="utf-8") as file:
                json.dump(t.lexer.data, file, indent=2, ensure_ascii=False)
            return t
    print("Esse produto não existe! Deseja adicionar um novo produto?")
    resposta = input("Y para sim/Qualquer outra combinação para não: ")
    if resposta.lower() == "y":
        nome = input(f"Insira o nome para o novo produto {produto_cod}: ")
        preco = round(float(input(f"Insira o preço para o novo produto {produto_cod}: ")),2)
        t.lexer.data['stock'].append({'cod': produto_cod, 'nome': nome, 'quantidade': quantidade, 'preco': preco})
        print(f"Produto {produto_cod} adicionado com sucesso")
        with open(argv[1], "w", encoding="utf-8") as file:
            json.dump(t.lexer.data, file, indent=2, ensure_ascii=False)
    else:
        print("Operação cancelada")
    return t

def t_SAIR(t):
    r'SAIR'
    euros = round(int(t.lexer.saldo),2)
    cents = round(int((t.lexer.saldo - euros) * 100),2)
    total_cents = euros * 100 + cents

    if total_cents != 0:
        coins = [200, 100, 50, 20, 10, 5, 2, 1]
        coin_names = ['2e', '1e', '50c', '20c', '10c', '5c', '2c', '1c']
        coin_counts = [0, 0, 0, 0, 0, 0, 0, 0]

        for i, coin in enumerate(coins):
            if total_cents >= coin:
                coin_counts[i] = total_cents // coin
                total_cents = total_cents % coin

        coin_strings = [f"{count} moeda de {coin_names[i]}" if count == 1 else f"{count} moedas de {coin_names[i]}" for i, count in enumerate(coin_counts) if count > 0]
        coins_output = ', '.join(coin_strings[:-1]) + ' e ' + coin_strings[-1] if len(coin_strings) > 1 else coin_strings[0]
        print(f"maq: Pode retirar o seu troco: {coins_output}.")
    else:
        print("maq: Não há troco para retirar.")

    print("maq: Até à próxima")
    t.lexer.flag = 1
    return t


def t_error(t):
    t.lexer.skip(1)

t_ignore = ' \t\n'

def main(argv):

    current_date = date.today()
    lexer = lex.lex()
    
    with open(argv[1], "r", encoding="utf-8") as file:
        data = json.load(file)

    lexer.data = data
    lexer.flag = 0
    lexer.saldo = 0

    total_stock = sum(item['quantidade'] for item in lexer.data['stock'])

    print(f"""
    maq: {current_date}, {total_stock} items em Stock, Estado atualizado.
    maq: Bom dia. Estou disponível para atender o seu pedido.
    Comandos disponíveis:
        - LISTAR
        - MOEDA <valor>, <valor> (separar entre vírgulas os valores e só aceita moedas de 2e, 1e, 50c, 20c, 10c, 5c, 2c e 1c)
        - SELECIONAR <item>
        - SALDO
        - ADICIONAR <item> <quantidade> (se não existir o item, é perguntado se quer adicionar um novo produto com o código inserido)
        - SAIR
        """)
    
    while lexer.flag == 0:
        input_user = input("Operação a realizar: ")
        lexer.input(input_user)
        token = lexer.token()
        if not token:
            print("Comando inválido")

    with open(argv[1], "w", encoding="utf-8") as file:
        json.dump(lexer.data, file, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    argv = sys.argv
    main(argv)