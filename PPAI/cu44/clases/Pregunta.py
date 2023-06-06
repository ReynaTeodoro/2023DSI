from clases.RespuestaPosible import respuestasPosiblesBD
preguntasBD = []
class Pregunta:
    def __init__(self, pregunta, respuestas):
        self.respuestas = respuestas
        self.pregunta = pregunta


    def getDescripcion(self):
        return self.pregunta

    def listarRespuestasPosibles(self):
        pass

    def obtenerEncuesta(self, listaDeEncuestas):
        for encuesta in listaDeEncuestas:
            if self in encuesta.preguntas:
                return encuesta.getDescripcionEncuesta()
        return "La pregunta no pertenece a ninguna encuesta"
    def __str__(self):
        return self.pregunta
