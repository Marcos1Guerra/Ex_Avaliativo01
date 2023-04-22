from pymongo import MongoClient
from database import Database
from model import PersonModel_Zoo

class ZoologicoCLI:
    def __init__(self, zoologico_dao):
        self.zoologico_dao = zoologico_dao

    def menu(self):
        print("Bem-vindo ao ZoologicoCLI!")
        while True:
            print("Escolha uma opção:")
            print("1. Listar animais")
            print("2. Adicionar um animal")
            print("3. Atualizar um animal")
            print("4. Excluir um animal")
            print("0. Sair")

            opcao = input()

            if opcao == 0:
                break
            elif opcao == 1:
                id = input("ID a ser lido: ")
                ZoologicoDAO.ler_animal(id);
            elif opcao == 2:
                ZoologicoDAO.criar_animal()
            elif opcao == 3:
                ZoologicoDAO.atualizar_animal()
            elif opcao == 4:
                id = input("ID a ser deletado: ")
                ZoologicoDAO.deletar_animal(id)
            else:
                print("Invalid choice")

class ZoologicoDAO:

    def __init__(self, db=Database):
        client = MongoClient("mongodb+srv://marcosguerra:<Pandorapandora1>@cluster0.fhmmjiw.mongodb.net/test")

    def criar_animal(self):
        nome = input("Nome do animal: ")
        especie = input("Espécie do animal: ")
        idade = int(input("Idade do animal: "))

        # criar objeto Habitat
        habitat_nome = input("Nome do habitat: ")
        habitat_tipoAmbiente = input("Tipo do habitat: ")

        # criar objeto Cuidador
        cuidador_nome = input("Nome do cuidador: ")
        cuidador_especialidade = input("Especialidade do cuidador: ")

        PersonModel_Zoo.criar_animais(nome, especie, idade, habitat_nome, habitat_tipoAmbiente, cuidador_nome, cuidador_especialidade)

    def ler_animal(self, id):
        PersonModel_Zoo.ler_animais(id)

    def atualizar_animal(self, animal):
        PersonModel_Zoo.atualizar_animais(animal.id, animal.nome, animal.especie, animal.idade)

    def deletar_animal(self, id):
        PersonModel_Zoo.deletar_animais(id);

class Cuidador:
    def __init__(self, id=None, nome=None, especialidade=None):
        self.id = id
        self.nome = nome
        self.especialidade = especialidade

class Habitat:
    def __init__(self, id=None, tipo=None, capacidade=None):
        self.id = id
        self.tipo = tipo
        self.capacidade = capacidade

class Animal:
    def __init__(self, nome=None, especie=None, habitat=None, cuidador=None, id=None):
        self.nome = nome
        self.especie = especie
        self.habitat = habitat
        self.cuidador = cuidador
        self.id = id