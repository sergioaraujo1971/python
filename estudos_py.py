import os
movies = ["The Holy Grail", "The Life of Brian", "The Meaning of Life"]
print(movies[1])
cast = ["Cleese", "Palin", "Jones", "Idle"]
print(cast)
print(len(cast))
print(cast[1])
cast.append("Gilliam")
print(cast)
print(len(cast))
print("exclui o último item da lista")
cast.pop()
print("Impressao da lista")
print(cast)
print("Tamanho da lista com a retirada do último item")
print(len(cast))
print("Inserindo novos itens à lista")
cast.extend(["Gillian", "Chapman"])
print("Impressao da lista")
print(cast)
print("Tamanho da lista com a retirada do último item")
print(len(cast))
print("Excluindo o Chapman do FIM da lista")
cast.remove("Chapman")
print("Impressao da lista")
print(cast)
print("Tamanho da lista com a retirada do último item")
print(len(cast))

print("Incluindo o Chapman do INICIO da lista")
cast.insert(0, "Chapman")
print("Impressao da lista")
print(cast)
print("Tamanho da lista com a retirada do último item")
print(len(cast))

# limpar a tela
print("\n" * os.get_terminal_size().lines)
# criar a lista de filmes preferidos e listá-los na tela
print("listar os filmes preferidos")
print("---------------------------")
print("uso de listas e iterações com o comando for")
print(" ")
print(" ")
filmes_favoritos = ["Star Wars I", "Star Wars II",
                    "Star Wars III", "Matrix I", "Ad Astra", "Mart", "Blade Runner"]
for each_filmes in filmes_favoritos:
    print(each_filmes)
