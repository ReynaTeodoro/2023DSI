from abc import ABC
from typing import List
class IAgregado(ABC):
    def crear_iterador(self,elementos:List[object]):
        return self
