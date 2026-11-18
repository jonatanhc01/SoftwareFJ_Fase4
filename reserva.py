from entidad import Entidad  # importa la clase base
from cliente import Cliente  # importa la clase de los clientes
from servicio import Servicio  # importa la clase de servicio
from excepciones import ErrorValidacion, ErrorReserva  # importa los errores de datos y reservas
from excepciones import ErrorDisponibilidad  # identifica servicios ocupados
from registro import logger  # permite guardar los cambios de estado

class Reserva(Entidad):  # creamos un clase de reserva
    def __init__(self, cliente, servicio, duracion):
        if not isinstance(cliente, Cliente):  # condicion, se ingreso un cliente
            raise ErrorValidacion("La reserva necesita un cliente valido.")

        if not isinstance(servicio, Servicio):  # condicion, se debe agregar un servicio
            raise ErrorValidacion("La reserva necesita un servicio valido.")

        try:  # comprueba la duración del servicio
            servicio.calcular_costo(duracion)
        except ErrorValidacion as error:  # error cuando la duracion es incorrecta o un valor equivocado
            raise ErrorReserva("No se pudo crear la reserva por su duración.") from error
        super().__init__()  # genera el identificador de la reserva
        self.__cliente = cliente  #  nos permite guardar el cliente
        self.__servicio = servicio  # nos permite guardar el servicio seleccionado
        self.__duracion = duracion  # nos permite guardar el tiempo solicitado
        self.__estado = "Pendiente"  # establecemos el estado inicial

    @property  # nos permite consultar el estado actual
    def estado(self):
        return self.__estado  # devuelve el estado de la reserva
    
    @property  # permite consultar el servicio de la reserva
    def servicio(self):
        return self.__servicio  # devuelve el servicio reservado

    def describir(self): # devuelve un resumen de la informacion de la reserva como cliente, servicio, duracion y el estado en que se encuentra
        return (
            f"Cliente: {self.__cliente.nombre} | "
            f"{self.__servicio.describir()} | "
            f"Duración: {self.__duracion} | "
            f"Estado: {self.__estado}"
        )  

    def confirmar(self):  # nos permite confirmar una reserva que esta en estado pendiente
        if self.__estado != "Pendiente":  # compruebamos el estado actual
            raise ErrorReserva("Solo se puede confirmar una reserva pendiente.") # muestra que solo podemos confirmar si esta en estado pendiente

        self.__estado = "Confirmada"  # cambiamos el estado actual de la reserva
        logger.info("Reserva confirmada: %s", self.identificador)
    def cancelar(self):  # nos permite cancelar una reserva pendiente o confirmada
        if self.__estado not in ("Pendiente", "Confirmada"): # si cumple las condiciones permite cambiar su estado
            raise ErrorReserva("La reserva no se puede cancelar en su estado actual.") # mustra que no cumple con las condiciones

        self.__estado = "Cancelada"  # cambiamos el estado de la reserva a cancelada
        logger.info("Reserva cancelada: %s", self.identificador)
    def procesar(self):  # nos permite completar una reserva confirmada
        if self.__estado != "Confirmada":  # condicion, comprueba que el estado este confirmada
            raise ErrorReserva("Solo se puede procesar una reserva confirmada.") # si no esta confrimada muestra por pantalla

        total = self.calcular_total()  # calculamos el costo antes de cambiar el estado de la reserva
        self.__estado = "Completada"  # cambiamos el estado de la reserva como completada
        logger.info("Reserva confirmada: %s", self.identificador)
        return total  # devuelve el valor del servicio

    def calcular_total(self, descuento=0, impuesto=0):  # nos permite calcular con o sin porcentajes para descuento o impusto
        for porcentaje in (descuento, impuesto):  # revisa los dos valores
            if isinstance(porcentaje, bool) or not isinstance(porcentaje, (int, float)):
                raise ErrorReserva("Los porcentajes deben ser numeros.")  # rechaza otros datos en caso de ingresar valores invalidos

            if not 0 <= porcentaje <= 100:  # nos permite ingresar porcentajes entre cero y cien
                raise ErrorReserva("Los porcentajes deben estar entre 0 y 100.")

        subtotal = self.__servicio.calcular_costo(self.__duracion)  # obtienos el costo del servicio
        con_descuento = subtotal * (1 - descuento / 100)  # aplica el descuento
        total = con_descuento * (1 + impuesto / 100)  # aplica el impuesto al valor descontado
        return round(total, 2)  # devuelve el total 