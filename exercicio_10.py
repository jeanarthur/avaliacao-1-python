def add_book(library, title, author):
    library.append({
        "title": title,
        "author": author
    })

def list_books(library):
    if not library or len(library) == 0:
        print("Sem livros cadastrados")
    else:
        for book in library:
            print(f"Título: {book['title']} - Autor: {book['author']}")

def find_book_by_title(library, title):
    if not library or len(library) == 0:
        print("Sem livros cadastrados")
    else:
        print("Resutado da Pesquisa: ")
        for book in library:
            if book['title'] == title:
                print(f"Título: {book['title']} - Autor: {book['author']}")
                return
        print("Livro não encontrado")

def get_number(message = "Digite um número: "):
    while True:
        try:
            value = int(input(message))
            return value
        except:
            print("Digite um valor válido!")

def main():
    library = []
    while True:
        print("1. Adicionar um livro")
        print("2. Listar todos os livros")
        print("3. Buscar um livro por título")
        print("4. Sair")
        value = get_number("Digite uma opção: ")

        match value:
            case 1:
                print("Cadastro de Livro: ")
                title = input("Nome do livro: ")
                author = input("Autor: ")
                add_book(library, title, author)
            case 2:
                print("Lista de Livros: ")
                list_books(library)
            case 3:
                print("Pesquisa: ")
                title = input("Nome do livro: ")
                find_book_by_title(library, title)
            case 4:
                print("Sistema finalizado")
                break
            case _:
                print("Escolha uma opção válida")
        print("")

main()