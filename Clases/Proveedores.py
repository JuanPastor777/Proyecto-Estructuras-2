class Proveedor:
    _contador_id = 1  # atributo de clase para generar IDs únicos

    def __init__(self, nombre, tipo_servicio, calificacion):
        self.id = Proveedor._contador_id
        Proveedor._contador_id += 1  # aumenta el contador para el siguiente proveedor
        self.calificacion = calificacion
        self.nombre = nombre
        self.tipo_servicio = tipo_servicio

    def __lt__(self, other):
        return self.id < other.id
    def __gt__(self, other):
        return self.id > other.id
    def __eq__(self, other):
        return  self.id == other.id
        
