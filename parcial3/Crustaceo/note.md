# Patron strategy
## Cuales son las estrategias posibles del calculo?
El actor elige que tipo de reclamo quiere hacer
Estrategias:
- tasa bruta 
- tasa critico
- tasa no critico
con sus formulas ver CU.2
## En que metodo se define cada estrategia se debe utilizar?
calcularTasaDeReclamo()
En la vista dinamica el Enganche se encuentra en la seleccion del tipo de tasa, como toda la logica de calculo se encuentra en el modelo, el controlador solo se encarga de llamar al metodo calcularTasaDeReclamo() del modelo y esto es lo que debemos modelar,
## Que responsabilidad denegamos?
Delegamos del gestor de reclamos la responsabilidad de calcular la tasa de reclamo, ya que el gestor de reclamos es el que conoce la estrategia de calculo de la tasa de reclamo.

El enganche se encuentra en el diagrama de secuencia desde generarReporteTasaReclamo() hasta buscarPedidosReclamosDeCliente() donde comienza el diagrama de secuencia que yo realice
