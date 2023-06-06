
from clases.CambioEstado import cambiosDeEstadoBD
from clases.Cliente import clientesBD
from clases.RespuestaDeCliente import respuestasDeClienteBD
llamadasBD = []

class Llamada:
    def __init__(self, descripcionOperador, detalleAccionRequerida, duracion, encuestaEnviada, ObservacionAuditor, respuestaDeEncuesta, cambioEstado, cliente):
        self.descripcionOperador = descripcionOperador
        self.detalleAccionRequerida = detalleAccionRequerida
        self.duracion = duracion
        self.encuestaEnviada = encuestaEnviada
        self.ObservacionAuditor = ObservacionAuditor
        # Este es un atributo referencial (cambioEstado va a ser una lista, ya que, la relación es un o muchos (? )
        self.cambiosDeEstado = cambioEstado
        self.respuestasDeEncuesta = respuestaDeEncuesta
        self.cliente = cliente

    def agregarCambioEstado(self, unCambioDeEstado):
        self.cambiosDeEstado.append(unCambioDeEstado)
        
    def agregarRespuestaDeEncuesta(self, respuestaEncuesta):
        self.respuestasDeEncuesta.append(respuestaEncuesta)

    def esDePeriodo(self, fechaInicio, fechaFin):
        for unCambioDeEstado in self.cambiosDeEstado:
            if unCambioDeEstado.esEstadoInicial():
                fechaHoraInicio = unCambioDeEstado.getFechaHoraInicio()
                if fechaInicio <= fechaHoraInicio and fechaHoraInicio <= fechaFin:
                    return True
        return False
    
    def tieneEncuestaRespondida(self):
        if len(self.respuestasDeEncuesta) > 0:
            return True


    def getDuracion(self):
        return self.duracion

    def getFechaHoraInicio(self):
        for unCambioDeEstado in self.cambiosDeEstado:
            if unCambioDeEstado.esEstadoInicial():
                return unCambioDeEstado.getFechaHoraInicio()
    def tieneRespuesta():
        pass

    def determinarUltimoEstado():
        pass

    def getNombreClienteLlamada(self):
        return self.cliente.getNombre()
    
    def determinarUltimoEstado(self):
        cambioEstadoActual = self.cambiosDeEstado[0]
        for cambioEstado in self.cambiosDeEstado:
            cambioEstadoActual = cambioEstado.esUltimoCambioEstado(cambioEstadoActual)
        return cambioEstadoActual.getNombreEstado()
    
    def getRespuestas(self):
        respuestas = []
        valoresSeleccionados = []
        for unaRespuesta in self.respuestasDeEncuesta:
            respuestas.append(unaRespuesta.getDescripcionRta())
            valoresSeleccionados.append(unaRespuesta.obtenerValorSeleccionado())
        return respuestas, valoresSeleccionados

    def mostrarDatosLlamada(self, listaDeEncuestas):
        nombreCliente = self.getNombreClienteLlamada()
        ultimoEstado = self.determinarUltimoEstado()
        duracion = self.getDuracion()
        preguntas, valoresSeleccionados = self.getRespuestas()
        encuesta = self.respuestasDeEncuesta[0].obtenerEncuesta(listaDeEncuestas)
        
        return {"nombreCliente": nombreCliente, 
                "ultimoEstado": ultimoEstado, 
                "duracion": duracion,
                "respuestas": preguntas, 
                "valoresSeleccionados": valoresSeleccionados,
                "encuesta":encuesta}

    def __str__(self):
        return self.descripcionOperador + " " + self.detalleAccionRequerida + " " + str(self.duracion) + " " + self.ObservacionAuditor + " " + str(self.cambiosDeEstado) +  str(self.cliente)
