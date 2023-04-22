from pymongo import MongoClient
from bson.objectid import ObjectId

class PersonModel_Zoo:
    def __init__(self, database):
        self.db = database
        self.collection = database.collection

    def criar_animais(self, nome: str, especie: str, idade: int, habitat_tipo: str, habitat_a: str, cuidador_nome: str, cuidador_espec) -> str:
        try:
            result = self.collection.insert_one({"Nome": nome, "Especie": especie, "Idade": idade, "Tipo ambiente": habitat_tipo, "Cuidador do ambiente": habitat_a, "Nome cuidador": cuidador_nome, "Especialidade": cuidador_espec})
            id_zoo = str(result.inserted_id)
            print(f"Person {nome} , {especie} , {idade} , {habitat_tipo}, {habitat_a} , {cuidador_nome} e {cuidador_espec} created with id: {id_zoo}")
            return id_zoo
        except Exception as error:
            print(f"An error occurred while creating Zoo: {error}")
            return None

    def ler_animais(self, id_zoo: str) -> dict:
        try:
            zoo = self.collection.find_one({"_id": ObjectId(id_zoo)})
            if zoo:
                print(f"Person found: {zoo}")
                return zoo
            else:
                print(f"No person found with id {id_zoo}")
                return None
        except Exception as error:
            print(f"An error occurred while reading person: {error}")
            return None

    def atualizar_animais(self, nome: str, especie: str, idade: int) -> int:
        try:
            result = self.collection.update_one({"nome": nome}, {"$set": {"Especie": especie, "Idade": idade}})
            if result.modified_count:
                print(f"Person {nome} atualizou especie {especie} e idade {idade}")
            else:
                print(f"No person found with id {nome}")
            return result.modified_count
        except Exception as error:
            print(f"An error occurred while updating person: {error}")
            return None

    def deletar_animais(self, id_zoo2: str) -> int:
        try:
            result = self.collection.delete_one({"_id": ObjectId(id_zoo2)})
            if result.deleted_count:
                print(f"Person {id_zoo2} deleted")
            else:
                print(f"No person found with id {id_zoo2}")
            return result.deleted_count
        except Exception as error:
            print(f"An error occurred while deleting person: {error}")
            return None