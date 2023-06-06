import csv
import sys
from clases.Llamada import llamadasBD
from clases.Encuesta import encuestasBD
from PyQt5.QtCore import QDate, QDateTime
import pandas as pd
class ControladorConsultaEncuesta:
    listaLlamadas = llamadasBD
    listaEncuestas = encuestasBD
    def consultarEncuesta(self, pantalla):
       self.fechaHoraInicio = None
       self.fechaHoraFin = None
       self.llamadasEnPeriodoRespondidas = []
       self.llamadaSeleccionada = None
       self.formatoSeleccionado = None
       self.datosLlamada = None
       self.seleccionFormato = None
       self.pantalla = pantalla

    def tomarSeleccionFechaInicio(self, fecha):
        self.fechaHoraInicio = fecha.toPyDateTime()

    def tomarSeleccionFechaFin(self, fecha):
        self.fechaHoraFin = fecha.toPyDateTime()

    def buscarLlamadasRespondidas(self):
        self.llamadasEnPeriodoRespondidas = []
        if len(self.listaLlamadas) > 0:
            for unaLlamada in self.listaLlamadas:
                if (unaLlamada.esDePeriodo(self.fechaHoraInicio, self.fechaHoraFin) and unaLlamada.tieneEncuestaRespondida()):
                    self.agregarLlamadaEnPeriodo(unaLlamada)
        
        self.pantalla.actualizarTablaLlamadas(self.llamadasEnPeriodoRespondidas)
        return self.llamadasEnPeriodoRespondidas
    def agregarLlamadaEnPeriodo(self, llamada_en_periodo):
        self.llamadasEnPeriodoRespondidas.append(llamada_en_periodo)

    def tomarSeleccionLlamada(self, llamadaSeleccionada):
        self.llamadaSeleccionada = llamadaSeleccionada
        self.obtenerDatosLlamada()

    def getDatosLlamada(self):
        return self.datosLlamada

    def obtenerDatosLlamada(self):
        # Aca obtenemos todas las encuestas
        self.datosLlamada = self.llamadaSeleccionada.mostrarDatosLlamada(self.listaEncuestas)
        self.pantalla.mostrarDatosLlamada(self.datosLlamada)
        return self.datosLlamada
    
    def tomarSeleccionFormato(self, seleccion):
        if seleccion == "CSV":
            self.generarInformeCSV()
        elif seleccion == "IMPRIMIR":
            self.generarImpresion()
        else:
            raise ValueError(f'No se puede imprimir en formato {seleccion!r}')
        

    def cancelarOperacion(self):
        raise SystemExit(0)

    def generarInformeCSV(self):
        if self.datosLlamada is None:
            raise ValueError('No hay datos :(')
        datosLlamada = self.datosLlamada
        df = pd.DataFrame(datosLlamada)
        df.to_csv('informe.csv', index=False)
        
    def generarImpresion(self):
        if self.datosLlamada is None:
            raise ValueError('No hay datos :(')
        datosLlamada = self.datosLlamada
        df = pd.DataFrame(datosLlamada)
        df.to_markdown('informe.md', index=False)
        
