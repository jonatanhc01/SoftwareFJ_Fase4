from entidad import Entidad  # importa la clase base Entidad 
import re  # permite comprobar el formato del correo
from excepciones import ErrorValidacion  # importa el error para datos incorrectos

class Cliente(Entidad):  # crea la clase para representar a los clientes que tiene como base entidad
    def __init__(self, nombre, correo):   # recibe el nombre al crear un cliente y tambien el correo
        if not isinstance(nombre, str):  # comprueba que el nombre sea texto
            raise ErrorValidacion("El nombre debe ser un texto.")

        nombre = nombre.strip()  # elimina los espacios del inicio y del final
        if len(nombre) < 2:  # rechaza nombres vacios o si son demasiado cortos, tienen que ser mayor de 2 caracters
            raise ErrorValidacion("El nombre debe tener al menos dos caracteres.")
        if not isinstance(correo, str):  # comprueba que el correo sea texto
            raise ErrorValidacion("El correo debe ser un texto.") # muestra error si no igresamos texto

        correo = correo.strip()  # elimina espacios al inicio y al final
        if not re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", correo):  # revisa el formato basico del correo
            raise ErrorValidacion("El correo debe tener un formato como nombre@dominio.com.")       
        super().__init__()  # ejecuta la parte que asigna el identificador automatico
        self.__nombre = nombre  # guarda el nombre en un atributo privado
        self.__correo = correo  # guarda el correo despues de validarlo

    @property  # nos permite consultar el nombre del cliente
    def nombre(self):
        return self.__nombre  # devuelve dato del nombre guardado

    def describir(self):  # define la descripcion que solicita la clase Entidad
        return f"Cliente: {self.__nombre}"  # devuelve una descripcion del cliente

    @property  # permite consultar el correo del cliente
    def correo(self):
        return self.__correo  # devuelve de los correos guardados actualmente