import sys
from ply import lex

#Lista dos tokens
tokens = (
    'COMMAND',
    'FROM',
    'WHERE',
    'VARS',
    'VALUES',
    'OPERATOR',
    'COMMA'
)

#Expressões regulares para os tokens
t_COMMAND = r'[Ss][Ee][Ll][Ee][Cc][Tt]|[Uu][Pp][Dd][Aa][Tt][Ee]|[Dd][Ee][Ll][Ee][Tt][Ee]'
t_FROM = r'[Ww][Hh][Ee][Rr][Ee]'
t_WHERE = r'[Ff][Rr][Oo][Mm]'
t_VARS = r'[A-Za-z]\w*'
t_VALUES = r'-?\d+'
t_OPERATOR = r'>=|<=|<|>|==|='
t_COMMA = r",|;"

t_ignore = ' \t'

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

def main(input, output):
    with open(input, 'r') as file:
        data = file.read()
        lexer = lex.lex()
        lexer.input(data)
        out = open(output, 'w')
        for token in lexer:
            out.write(f'{token}\n')

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])