from entidad import Entidad  # importa la clase base del sistema
from abc import abstractmethod  # permite definir metodos que completara cada tipo de servicio en este caso abstracto
from excepciones import ErrorValidacion  # importa el error para datos incorrectos


class Servicio(Entidad):  # crea una clase servicio que tendra como base entidad 
    def __init__(self, nombre, tarifa):
        if not isinstance(nombre, str):  # comprueba que el nombre sea texto
            raise ErrorValidacion("El nombre del servicio debe ser un texto.")

        nombre = nombre.strip()  # elimina espacios al inicio y al final
        if not nombre:  # condicion que no permite no permite que se ingrese un nombre vacio
            raise ErrorValidacion("El servicio debe tener un nombre.") # muestra por pantalla aviso de que debe haber un nombre

        if isinstance(tarifa, bool) or not isinstance(tarifa, (int, float)): # condicion que permite que solo se ingresen valores int en esta caso que solo sean numeros
            raise ErrorValidacion("La tarifa debe ser un numero.") 

        if not 0 < tarifa < float("inf"):  # solicitamos que la tarifa sea positiva y finita
            raise ErrorValidacion("La tarifa debe ser mayor que cero y finita.")

        super().__init__()  # genera el identificador del servicio
        self.__nombre = nombre  # permite guardar el nombre del servicio
        self.__tarifa = tarifa  # permite guardar su tarifa

    @property  # permite consultar el nombre
    def nombre(self):
        return self.__nombre  # devuelve el nombre guardado

    @property  # permite consultar la tarifa
    def tarifa(self):
        return self.__tarifa  # devuelve la tarifa guardada

    @abstractmethod  # cada tipo de servicio definira como calcular su costo
    def calcular_costo(self, duracion):
        pass  # el calculo se completara en las clases de cada servicio

class Sala(Servicio):  # creamos una clase llamada sala que para el alquiler de la sala 
    def describir(self):
        return f"Sala: {self.nombre}"  # devuelve el nombre de la sala

    def calcular_costo(self, duracion):
        if isinstance(duracion, bool) or not isinstance(duracion, (int, float)): #  condicion que permitira solo eel ingreso de numeros
            raise ErrorValidacion("La duracion debe ser un numero.")  

        if not 0 < duracion < float("inf"): # permite que el valor permitido sea solo mayor a 0 
            raise ErrorValidacion("La duración debe ser mayor que cero y finita.")  

        return self.tarifa * duracion  # multiplicamos la tarifa por las horas de uso

class Equipo(Servicio):  # creamos una clase llamada equipo que para el alquiler del equipo
    def describir(self):
        return f"Equipo: {self.nombre}"  # devuelve el nombre del equipo

    def calcular_costo(self, duracion):
        if isinstance(duracion, bool) or not isinstance(duracion, int): # permite que solo se agregue un valor correcto en este caso entero
            raise ErrorValidacion("La duracion debe ser un numero entero de dias.")  

        if duracion <= 0:
            raise ErrorValidacion("La duracion debe ser mayor que cero.")  # condicion permite que no se agrege una duracion invalida

        return self.tarifa * duracion  # multiplica la tarifa diaria por los dias

class Asesoria(Servicio):  # creamos una clase llamada asesoria
    def describir(self):
        return f"Asesoría: {self.nombre}"  # devuelve el nombre de la asesoria

    def calcular_costo(self, duracion):
        if isinstance(duracion, bool) or not isinstance(duracion, (int, float)):
            raise ErrorValidacion("La duracion debe ser un numero.")  # comprueba que sean horas

        if not 0 < duracion < float("inf"):
            raise ErrorValidacion("La duracion debe ser mayor que cero y finita.")  # permite que solo se ingresen valores validos

        return self.tarifa * duracion  # calcula el costo segun las horas de asesoria       