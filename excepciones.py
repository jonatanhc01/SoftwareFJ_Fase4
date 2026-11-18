class ErrorValidacion(ValueError):  # representara los datos incorrectos
    pass  # conservara el comportamiento de ValueError


class ErrorReserva(ValueError):  # representa operaciones incorrectas sobre reservas
    pass  # conservara el comportamiento de ValueError


class ErrorDisponibilidad(ErrorReserva):  # representa un servicio cuando no esta disponible
    pass  # conservara el comportamiento de ErrorReserva