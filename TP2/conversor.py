import sys
import re

def conversor(md):

    #Tratamento dos cabeçalhos
    md = re.sub(r'^# (.+)$', r'<h1>\1</h1>', md, flags=re.M)
    md = re.sub(r'^## (.+)$', r'<h2>\1</h2>', md, flags=re.M)
    md = re.sub(r'^### (.+)$', r'<h3>\1</h3>', md, flags=re.M)

    #Tratamento dos negritos
    md = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', md)

    #Tratamento do itálico
    md = re.sub(r'\*(.+?)\*', r'<i>\1</i>', md)

    #Tratamento dos blockquotes
    md = re.sub(r'^(?:> (.*?)|>)(?:\n\n|\n(?=>)|\Z)', r'<p><blockquote>\1</blockquote></p>', md, flags=re.S|re.M)

    #Tratamento das listas ordenadas
    md = re.sub(r'(?<=\n)(\d+\.) (.+?)(?=\n\n|\n\s*\d+\.)', r'<li>\2</li>', md)
    md = re.sub(r'(\n<li>.+?</li>)+', r'\n<ol>\g<0>\n</ol>', md)

    #Tratamento dos blocos de código
    md = re.sub(r'`(.+?)`', r'<p><code>\1</code></p>', md)

    #Tratamento da horizontal rule
    md = re.sub(r'^---*$', r'<hr>', md, flags=re.M)

    #Tratamento das imagens (tem de vir antes dos links senão causa problemas)
    md = re.sub(r'!\[(.*?)\]\((.*?)\)', r'<img src="\2" alt="\1">', md)

    #Tratamento dos links
    md = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', md)

    #Criação da página html em concreto com o conteúdo md que acabamos de converter
    html = f'''<!DOCTYPE html>\n
    <html>\n
    <head>\n
    <title>Conversor</title>\n
    </head>\n
    <body>\n
    {md}\n
    </body>\n
    </html>\n
    '''
    
    return html #Envio do novo html convertido

def main(argv):
    # Leitura do ficheiro md colocado nos argumentos na execução
    if len(argv) == 2 and argv[1].endswith(".md"):
        with open(argv[1], "r", encoding='utf-8') as f:
            md = f.read()
        #Escrita desse ficheiro md no novo ficheiro htm
        with open(argv[1].replace(".md", ".html"), "w", encoding="utf-8") as html:
            html.write(conversor(md)) #Chamada da função conversora do ficheiro
    else:
        print("Ficheiro md não introduzido ou encontrado")

if __name__ == "__main__":
    main(sys.argv)