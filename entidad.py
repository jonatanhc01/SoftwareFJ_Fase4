from abc import ABC, abstractmethod  # importa las herramientas necesarias para crear una clase abstracta


class Entidad(ABC):  # crea una clase base para los elementos del sistema
    def __init__(self):  # se ejecutara al crear una entidad
        from uuid import uuid4  # importamos el generador de identificadores
        self.__identificador = str(uuid4())  # asigna un identificador automatico

    @property  # permite consultar el identificador como un atributo
    def identificador(self):
        return self.__identificador  # devuelve el dato en este caso el identificador 

    @abstractmethod  # indica que cada clase derivada debe definir su descripcion
    def describir(self):
        pass  # la descripcion se implementara en cada clase 