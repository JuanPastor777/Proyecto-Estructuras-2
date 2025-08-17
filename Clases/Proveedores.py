class Proveedor:
    _contador_id = 1  # atributo de clase para generar IDs únicos

    def __init__(self, nombre, tipo_servicio, calificacion):
        self.id = Proveedor._contador_id
        Proveedor._contador_id += 1  # aumenta el contador para el siguiente proveedor
        self.calificacion = calificacion
        self.nombre = nombre
        self.tipo_servicio = tipo_servicio
        
