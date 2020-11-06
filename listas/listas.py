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
                    "Star Wars III", "Matrix I", "Ad Astra", "The Martian", "Blade Runner"]
for each_filmes in filmes_favoritos:
    print(each_filmes)
# Star Wars I - lançado em 1999
# Star Wars II - lançado em 2002
# Star Wars III - lançado em 2005
# Matrix I - lançado em 1999
# Ad Astra - lançado em 2019
# The Martian - lançado em 2015
# Blade Runner - lançado em 1982
# lista de filmes melhorada
# criar a lista de filmes preferidos e listá-los na tela
print("listar os filmes preferidos mais atualizada")
print("-------------------------------------------")
print("uso de listas e iterações com o comando for")
print(" ")
print(" ")
filmes_favoritos_completo = ["Star Wars I", 1999,
                             "Star Wars II", 2002,
                             "Star Wars III", 2005,
                             "Matrix I", 1999,
                             "Ad Astra", 2019,
                             "The Martian", 2015,
                             "Blade Runner", 1982,
                             ["Alien I", 1978,
                              "Alien II", 1984]]
for each_filmes in filmes_favoritos_completo:
    if isinstance(each_filmes, list):
        for novoeach_filmes in each_filmes:
            print(novoeach_filmes)
    else:
        print(each_filmes)
