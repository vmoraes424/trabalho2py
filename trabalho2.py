from bs4 import BeautifulSoup
import requests
import re
from collections import Counter

musicas = []
url = "https://www.revistabula.com/9517-as-100-melhores-musicas-de-todos-os-tempos/"

def listar():
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")

    div = soup.find("div", class_="shortcode-featured-content")

    if div:
        ps = div.find_all("p")

        global musicas
        for p in ps:
            if p.text.strip():
                musicas.append(p.text.strip())

        for i, titulo in enumerate(musicas):
            print(f"{i + 1}. {titulo}")

    else:
        print("Div não encontrada na página.")

def agrupar():
    global musicas
    if musicas:
        palavras = re.findall(r'\b\w+\b', ' '.join(musicas).lower())
        palavras_contadas = Counter(palavras)
        for palavra, count in palavras_contadas.most_common(10):
            print(f"Palavra: {palavra} - Frequência: {count}")
    else:
        print("Não há músicas para apresentar.")


def conjunto():
    global musicas
    if musicas:
        palavras = re.findall(r'\b\w+\b', ' '.join(musicas).lower())
        common_words = set(word for word, count in Counter(palavras).items() if count > 1)

        print("Palavras comuns entre os títulos das músicas:")
        for word in common_words:
            print(word)
    else:
        print("Não há músicas para apresentar.")

def pesquisarDados():
    global musicas
    if musicas:
        palavra_chave = input("Digite a palavra-chave para pesquisar: ").strip().lower()

        musicas_encontradas = [title for title in musicas if palavra_chave in title.lower()]

        if musicas_encontradas:
            print(f"Músicas que contêm a palavra-chave '{palavra_chave}':")
            for musica in musicas_encontradas:
                print(musica)
        else:
            print(f"Nenhuma música encontrada com a palavra-chave '{palavra_chave}'.")
    else:
        print("Não há músicas para apresentar.")

while True:
    print("")
    print("1 - Listar")
    print("2 - Agrupar")
    print("3 - Conjunto")
    print("4 - Pesquisar Dados")
    print("5 - Sair")
    print("")
    user_input = input("Digite a opção que deseja: ")
    if user_input == "1":
        listar()
    elif user_input == "2":
        agrupar()
    elif user_input == "3":
        conjunto()
    elif user_input == "4":
        pesquisarDados()
    elif user_input == "5":
        break
