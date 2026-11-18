from cliente import Cliente  # importa la clase de los clientes
from servicio import Servicio  # importa la base de los servicios
from excepciones import ErrorValidacion  # importa el error para datos incorrectos
from registro import logger  # permite registrar las operaciones
from reserva import Reserva
from excepciones import ErrorDisponibilidad

class Sistema:  # organiza los datos de la aplicación
    def __init__(self):
        self.__clientes = []  # guarda los clientes registrados
        self.__servicios = []  # guarda los servicios registrados
        self.__reservas = []  # guarda las reservas del sistema

    def agregar_cliente(self, cliente):
        if not isinstance(cliente, Cliente):  # comprueba que se este ingresando un cliente
            raise ErrorValidacion("Debe agregar un cliente valido.")

        if cliente in self.__clientes:  # ayuda que no se pueda guardar el mismo cliente
            raise ErrorValidacion("El cliente ya esta registrado.")

        self.__clientes.append(cliente)  # agrega el cliente a la lista de clientes
        logger.info("Cliente registrado: %s", cliente.identificador)  # muestra que fue registrado y hace su operacion de guardado

    def agregar_servicio(self, servicio):
        if not isinstance(servicio, Servicio):  # comprueba que se esta ingresando un servicio
            raise ErrorValidacion("Debe agregar un servicio valido.")

        if servicio in self.__servicios:  # ayuda que no se pueda guardar el mismo servicio
            raise ErrorValidacion("El servicio ya esta registrado.")

        self.__servicios.append(servicio)  # agrega el servicio a la lista 
        logger.info("Servicio registrado: %s", servicio.identificador)  # muestra que fue registrado y hace su operacion de guardado

    def resumen(self): # da una descripcion de elementos registrados
        return (
            f"Clientes: {len(self.__clientes)} | "
            f"Servicios: {len(self.__servicios)} | "
            f"Reservas: {len(self.__reservas)}"
        )  
    
    def crear_reserva(self, cliente, servicio, duracion):
        try:  # comprueba los datos y si el cliente ingresado no esta registrado 
            if cliente not in self.__clientes:
                raise ErrorValidacion("El cliente no esta registrado.")

            if servicio not in self.__servicios: # comprueba los datos y si el servicio ingresado no esta registrado 
                raise ErrorValidacion("El servicio no esta registrado.")

            for reserva in self.__reservas:  # revisa las reservas que estan guardadas para conocer su estado
                if reserva.servicio is servicio and reserva.estado in ("Pendiente", "Confirmada"):
                    raise ErrorDisponibilidad("El servicio tiene una reserva activa.")

            nueva_reserva = Reserva(cliente, servicio, duracion)  # crea la reserva
        except ValueError:  # registra el problema y lo comunica al código que llamó
            logger.exception("No se pudo registrar la reserva")
            raise  # conserva el error original
        else:
            self.__reservas.append(nueva_reserva)  # guarda solo una reserva válida
            logger.info("Reserva registrada: %s", nueva_reserva.identificador)
            return nueva_reserva  # permite consultar y gestionar la reserva    

        