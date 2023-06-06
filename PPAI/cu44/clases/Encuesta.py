from clases.Pregunta import preguntasBD
encuestasBD = []
class Encuesta:
    def __init__(self, fechaFinVigencia, descripcion, preguntas):
        self.preguntas = []
        self.descripcion = descripcion
        self.fechaFinVigencia = fechaFinVigencia
        self.preguntas = preguntas

    def agregarPreguntas(self, unPregunta):
        self.preguntas.append(unPregunta)

    def getDescripcionEncuesta(self):
        return self.descripcion
    def __str__(self):
        return self.descripcion
