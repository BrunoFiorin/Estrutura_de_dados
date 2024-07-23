class Livro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.proximo = None  # Ponteiro para o próximo livro na pilha

class Pilha:
    def __init__(self):
        self.topo = None  # Início da pilha
        self.tamanho = 0  # Tamanho da pilha

    def add(self, l):
        l.proximo = self.topo  # O próximo livro é o atual topo da pilha
        self.topo = l  # O livro adicionado se torna o novo topo da pilha
        self.tamanho += 1  # Incrementa o tamanho da pilha
        print(f"Livro '{l.titulo}' adicionado à pilha.")

    def remover(self):
        if self.topo is None:
            print("A pilha está vazia. Nenhum livro para remover.")
            return None

        livro_removido = self.topo
        self.topo = self.topo.proximo  # O novo topo é o próximo livro da pilha
        self.tamanho -= 1  # Decrementa o tamanho da pilha
        print(f"Livro '{livro_removido.titulo}' removido da pilha.")
        return livro_removido

    def imprimir(self):
        if self.topo is None:
            print("A pilha está vazia.")
            return

        print("Livros na pilha:")
        atual = self.topo
        while atual is not None:
            print(f"Título: {atual.titulo}, Autor: {atual.autor}, Páginas: {atual.paginas}")
            atual = atual.proximo

def main():
    pilha_de_livros = Pilha()

    while True:
        print("\nMenu de Opções:")
        print("1. Adicionar livro")
        print("2. Remover livro")
        print("3. Imprimir pilha de livros")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            titulo = input("Digite o título do livro: ")
            autor = input("Digite o autor do livro: ")
            paginas = int(input("Digite o número de páginas do livro: "))
            livro = Livro(titulo, autor, paginas)
            pilha_de_livros.add(livro)
        elif opcao == "2":
            pilha_de_livros.remover()
        elif opcao == "3":
            pilha_de_livros.imprimir()
        elif opcao == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
