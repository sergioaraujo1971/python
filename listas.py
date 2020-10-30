# programa listas.py
# autor : Sergio A Araujo
# escrito em 29 de outubro de 2020

# importando o módulo do sistema operacional Windows
import os
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
