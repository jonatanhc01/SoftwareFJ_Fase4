from cliente import Cliente  # importa la clase que representa a los clientes
from servicio import Sala, Equipo, Asesoria  # importa los tres tipos de servicios
from reserva import Reserva  # importa la clase para crear reservas
from registro import logger  # importa el registrador de eventos
from excepciones import ErrorReserva  # importa el error de las reservas
from sistema import Sistema  # importa la clase que organiza la aplicación


cliente = Cliente("jonatan", "jonatan@prueba.com")  # crea un cliente de prueba y un correo
print(cliente.describir())  # muestra la descripcion del cliente creado
print("Identificador:", cliente.identificador)  # muestra el identificador automatico

try:  # intenta crear un cliente con un nombre vacio
    cliente_invalido = Cliente("   ", "jonatan@prueba.com")  # crea uno cliente invalido en este caso son solo espacios
except ValueError as error:  # comprueba el problema para continuar la ejecucion
    logger.error("%s: %s", type(error).__name__, error)  # guarda el error en eventos.log
    print("No se pudo crear el cliente:", error)  # mostrara en el terminal la razon del error

print("La prueba termino y el programa continua.")  # muestra que la prueba termino

try:  # intenta crear un cliente con un correo incorrecto
    otro_cliente = Cliente("Luis", "correo_incorrecto")
except ValueError as error:  # comprueba el error del correo
    logger.error("%s: %s", type(error).__name__, error)  # guarda el error en eventos.log
    print("Correo rechazado:", error)

clientes = []  # permite crear una lista para guardar los clientes que creamos
clientes.append(cliente)  # agrega el cliente que ya habiamos creado

nuevo_cliente = Cliente("Yuna", "Yuna@example.com")  # crea otro cliente 
clientes.append(nuevo_cliente)  # agregamos el segundo cliente a la lista

print("\nClientes registrados:")  # muestra el titulo separado de las pruebas anteriores
for persona in clientes:  # hace un chequeo de los clientes guardados 
    print(persona.describir())  # muestra la descripcion de cada cliente
    print("Correo:", persona.correo)  # muestra su correo

print("Total de clientes:", len(clientes))  # muestra cuantos clientes estan guardados

sala = Sala("Sala de reuniones", 25000)  # establece una tarifa de 25000 por hora
print("\n", sala.describir())  # muestra la descripcion
print("Costo por 3 horas:", sala.calcular_costo(3))  # calcula el costo

equipo = Equipo("Proyector", 40000)  # establece una tarifa de 40000 por dia
print("\n", equipo.describir())  # muestra el equipo seleccionado
print("Costo por 2 dias:", equipo.calcular_costo(2)) # muestra el costo del alquiler total

asesoria = Asesoria("Soporte informatico", 60000)  # tarifa de 60000 COP por hora
print("\n", asesoria.describir())  # muestra la asesori a seleccionada
print("Costo por 1.5 horas:" , asesoria.calcular_costo(1.5))  # calcula una hora y media

reserva = Reserva(cliente, sala, 3)  # reserva la sala para el cliente se establecio 3 horas
print("\nReserva creada:")  # muestra el titulo de la prueba
print(reserva.describir())  # muestra los datos de la reserva
print("Total:", reserva.calcular_total())  # muestra el costo total de la reserva

reserva.confirmar()  # permite confirmar la reserva que habiamos creado
print("Despues de confirmar:", reserva.estado)  # muestra en pantalla el nuevo estado actual

reserva.cancelar()  # permite cancelar la reserva confirmada
print("Después de cancelar:", reserva.estado)  # muestra el estado cancelado

try:  # intenta confirmar una reserva que ya fue cancelada
    reserva.confirmar()
except ValueError as error:  # controla el error para que el programa continue
    logger.error("%s: %s", type(error).__name__, error)  # guarda el error en eventos.log
    print("no puede ser rechazada:", error)  # muestra que la reserva no puede ser rechazada 

print("La prueba de estados termino.")  # muestra por pantalla

otra_reserva = Reserva(nuevo_cliente, equipo, 3)  # realiza la reserva del proyector para Yuna durante 3 dias
otra_reserva.confirmar()  # confirmamos la nueva reserva
total = otra_reserva.procesar()  # completa la reserva y obtenemos su costo

print("\nReserva procesada:")  # muestra el estado reserva procesada
print(otra_reserva.describir())  # muestra los datos y el estado final
print("Total:", total)  # muestra el costo total del servicio

try:  # intenta procesar nuevamente la misma reserva
    otra_reserva.procesar()
except ValueError as error:  # controla la operacion incorrecta
    print("proceso rechazado:", error)  # muestra por pantalla
    logger.error("%s: %s", type(error).__name__, error)  # guarda el error en eventos.log

reserva_calculo = Reserva(cliente, sala, 3)  # crea una reserva para probar los porcentajes

print("\nPrueba de descuento e impuesto:")  # muestra en pantalla
print("Total sin ajustes:", reserva_calculo.calcular_total())  # calcula sin ningun porcentaje
print("Con descuento del 10%:", reserva_calculo.calcular_total(descuento=10))  # aplica descuento de 10% y un porcentaje de 5% en impuestos
print("Con descuento del 10% e impuesto del 5%:",
      reserva_calculo.calcular_total(descuento=10, impuesto=5))  # aplica ambos porcentajes

pruebas_servicios = [(sala, 3), (equipo, 2), (asesoria, 1.5)]  # reúne servicios con sus duraciones

print("\nPrueba de los diferentes servicios:")  # muestra el titulo de la prueba
for servicio, duracion in pruebas_servicios:  # recorre cada servicio y su duracion
    print(servicio.describir())  # usa la descripcion de cada tipo de servicio
    print("Costo:", servicio.calcular_costo(duracion))  # calculamos el costo de cada servicio

logger.info("Las pruebas iniciales terminaron correctamente.")  # guarda un evento informativo
print("\nRegistro guardado en eventos.log")  # indica donde podemos consultar el registro guardado

for dias in (2, -1):  # probamos una duracion de 2 dias y tambien otra incorrecta -1
    try:  # intentamos crear una reserva del equipo
        prueba_reserva = Reserva(cliente, equipo, dias)
    except ErrorReserva as error:  # controla el fallo al crear la reserva
        print("Reserva rechazada:", error)
        print("Causa original:", error.__cause__)  # muestra la causa del problema
        logger.exception("Error al reservar el equipo")  # guarda el error y su causa
    else:  # se ejecuta unicamente si la reserva se creo correctamente
        print("Reserva valida. Total:", prueba_reserva.calcular_total())
        logger.info("Reserva de equipo creada para %s días.", dias)  # registra la creacion de la reserva
    finally:  # se ejecuta si hubo un error o no
        print("Intento de reserva finalizado.\n")

sistema = Sistema()  # crea el sistema con sus listas vacias
sistema.agregar_cliente(cliente)  # registra al cliente llamado Jonatan
sistema.agregar_cliente(nuevo_cliente)  # registra a la cliente llamada Yuna

for servicio in (sala, equipo, asesoria):  # recorre los tres servicios creados
    sistema.agregar_servicio(servicio)  # registra cada servicio

print("\nResumen del sistema:")  # muestra un resumen de los datos ingresados
print(sistema.resumen())  # muestra las cantidades registradas

reserva_sistema = sistema.crear_reserva(cliente, sala, 3)  # creamos y registramos una reserva de sala
print("\nReserva registrada:", reserva_sistema.describir())

try:  # intenta reservar el mismo servicio mientras ya esta en uso
    sistema.crear_reserva(nuevo_cliente, sala, 2)
except ErrorReserva as error:  # genera un error ErrorDisponibilidad
    print("No disponible:", error)  # muestra el motivo en este caso que no esta disponible

print(sistema.resumen())  # muestra un resumen de las reservas 

reserva_sistema.cancelar()  # permite cancelar la reserva que ocupaba la sala
print("\nEstado de la primera reserva:", reserva_sistema.estado) # muestra el estado de la reserva

nueva_reserva_sala = sistema.crear_reserva(nuevo_cliente, sala, 2)
print("Nueva reserva:", nueva_reserva_sala.describir())  # muestra la nueva reserva 
print("Total:", nueva_reserva_sala.calcular_total())  # calcula dos horas de sala
print(sistema.resumen()) # muestra un resumen de las reservas

print("\nPrueba de tarifa invalida:")

try:
    servicio_invalido = Sala("Sala de capacitacion", -25000)
except ValueError as error:
    print("Servicio rechazado:", error)  # muestra por que no se creo
    logger.error("%s: %s", type(error).__name__, error)  # registra el error en eventos log

print("El programa continua despues de la prueba.")