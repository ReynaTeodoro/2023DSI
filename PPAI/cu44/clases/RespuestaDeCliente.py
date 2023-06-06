from clases.RespuestaPosible import respuestasPosiblesBD
respuestasDeClienteBD = []

class RespuestaDeCliente:
    def __init__(self, fechaEncuesta, respuestaSeleccionada):
        self.fechaEncuesta = fechaEncuesta
        self.respuestaSeleccionada = respuestaSeleccionada
    
    def getDescripcionRta(self):
        return self.respuestaSeleccionada.getDescripcionRta()

    def obtenerValorSeleccionado(self):
        return self.respuestaSeleccionada.getValor()
    def obtenerEncuesta(self, listaDeEncuestas):
        return self.respuestaSeleccionada.obtenerEncuesta(listaDeEncuestas)

    def getRespuesta(self):
        return self
    def __str__(self):
        return self.getDescripcionRta()
