from interface import Observador

class Interessados(Observador):

    def _init_(self, nome, email):
        self.nome = nome
        self.email = email
    def update_add(self):
        print(f'Estou informando o {self.nome} no mel (self.email)')
        pass
