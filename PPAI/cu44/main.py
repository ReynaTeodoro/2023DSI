import sys

from clases.ControlConsultarEncuesta import ControladorConsultaEncuesta
from clases.pantallaConsultarEncuesta import Ui_PantallaConsultarEncuesta
from generador import GeneradorAleatorio
from PyQt5 import QtWidgets


def main() -> int:
    #populate de los datos
    generador = GeneradorAleatorio()
    generador.inicializar()
    #habilita Pantalla:
    app = QtWidgets.QApplication(sys.argv)
    PantallaConsultarEncuesta = QtWidgets.QMainWindow()
    ui = Ui_PantallaConsultarEncuesta()
    #iniciamos el controlador
    controlador = ControladorConsultaEncuesta()
    controlador.consultarEncuesta(ui)

    ui.habilitarPantalla(PantallaConsultarEncuesta,controlador)
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
    
    







