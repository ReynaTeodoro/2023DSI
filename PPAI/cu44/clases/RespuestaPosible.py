respuestasPosiblesBD = []
class RespuestaPosible:
    def __init__(self, descripcion, valor):
        self.descripcion = descripcion
        self.valor = valor

    def getRespuesta(self):
        return self
    def getValor(self):
        return self.valor
    def getDescripcionRta(self):
        return self.descripcion
    
    def obtenerEncuesta(self, listaDeEncuestas):
        for unaEncuesta in listaDeEncuestas:
            for unaPregunta in unaEncuesta.preguntas:
                if self in unaPregunta.respuestas:
                    return unaPregunta.obtenerEncuesta(listaDeEncuestas)





            if self in unaEncuesta.preguntas:
                return unaEncuesta.nombre
        return "La pregunta no pertenece a ninguna encuesta"
    

    def __str__(self):
        return self.descripcion
