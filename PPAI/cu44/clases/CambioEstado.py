from clases.Estado import estadosBD
cambiosDeEstadoBD = []


class CambioEstado:
    # El atributo estado es un objeto de la clase Estado
    def __init__(self, fechaHoraInicio, estado):
        self.fechaHoraInicio = fechaHoraInicio
        self.estado = estado

    def esEstadoInicial(self):
        if self.estado.esIniciada():
            return True
        else:
            return False

    def getFechaHoraInicio(self):
        return self.fechaHoraInicio
    
    def getNombreEstado(self):
        # Aca le pedimos al estado el nombre ... Envio de mensajes
        return self.estado.getNombre()
    
    def obtenerEstadoActual(self):
        # Aca obtenemos el estado actual
        return self.estado
    
    def esUltimoCambioEstado(self, unCambioEstado):
        if self.fechaHoraInicio > unCambioEstado.fechaHoraInicio:
            return self
        return unCambioEstado
    def __str__(self):
        return str(self.fechaHoraInicio) + " " + self.estado.getNombre()
