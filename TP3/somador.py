import sys
import re

regex = r'(?P<sum>-?\d+)|(?P<on>[Oo][Nn])|(?P<off>[Oo][Ff]{2})|(?P<show>=)'

def main(file_path):
    state = False
    soma = 0

    with open(file_path, 'r') as file:
        for line in file:
            for match in re.finditer(regex, line, flags=re.IGNORECASE):
                if match.group('sum'):
                    if state:
                        soma += int(match.group('sum'))
                elif match.group('on'):
                    state = True
                elif match.group('off'):
                    state = False
                elif match.group('show'):
                    print("SOMA: " + str(soma) + "\n")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python programa.py <caminho_para_arquivo>")
    else:
        main(sys.argv[1])
                    