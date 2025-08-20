class Proveedor:
    _contador_id = 1  # atributo de clase para generar IDs únicos

    def __init__(self, nombre, tipo_servicio, ubucacion, calificacion):
        self.id = Proveedor._contador_id
        Proveedor._contador_id += 1  # aumenta el contador para el siguiente proveedor
        self.calificacion = calificacion
        self.nombre = nombre
        self.tipo_servicio = tipo_servicio
        self.ubucacion = ubucacion
    def __str__(self):
        estrellas = "★" * int(self.calificacion) + "☆" * (5 - int(self.calificacion))
        return f"ID:{self.id} Nombre: {self.nombre} Servicio: {self.tipo_servicio} Ubicacion:{self.ubucacion}  Calificacion: {estrellas} {self.calificacion}"


    def __repr__(self):
        return str(self)

    def __lt__(self, other):
        return self.id < other.id
    def __gt__(self, other):
        return self.id > other.id
    def __eq__(self, other):
        return  self.id == other.id
        
