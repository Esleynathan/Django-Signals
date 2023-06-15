from abc import ABC, abstractclassmethod

class Observador(ABC):
    @abstractclassmethod
    def update_add(self):
        pass
    
