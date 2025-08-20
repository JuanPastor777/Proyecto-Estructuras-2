from Arbol.Arbol import BTree
from Clases.Proveedores import Proveedor

if __name__ == "__main__":
   
    tree = BTree(4)

    while True:
        print("\n     MENÚ PARA GESTIÓN DE PROVEEDORES  ")
        print(" 1. Registrar proveedor               ")
        print(" 2. Buscar por tipo de servicio       ")
        print(" 3. Mostrar proveedores por nombre    ")
        print(" 4. Mostrar proveedores por calificación ")
        print(" 5. Salir ")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            print("\n--- Registro de nuevo proveedor ---")
            try:
                nombre = input("Nombre del proveedor: ")
                tipo_servicio = input("Tipo de servicio: ")
                ubicacion = input("Ubicación: ")
                calificacion = int(input("Calificación (1 a 5 estrellas): "))

                if calificacion < 1 or calificacion > 5:
                    print("La calificación debe ser entre 1 y 5.\n")
                    continue

                # Crear el objeto Proveedor 
                nuevo_proveedor = Proveedor(nombre, tipo_servicio, ubicacion, calificacion)
                
                # Insertar el nuevo proveedor en el arbol 
                tree.insert(nuevo_proveedor)

                print(f"Proveedor registrado correctamente con ID {nuevo_proveedor.id}")
                print(f"Datos almacenados: {nuevo_proveedor.__dict__}\n")

            except ValueError:
                print("Ingresa un valor válido.\n")
                
        elif opcion == "2":
            servicio = input("Ingrese el tipo de servicio a buscar: ").lower()
            resultados = tree.search_by_service(servicio)
            orden = input("Ingrese  para mostrar en orden (c) para calificacion o (n) para nombre: ").lower()
            while orden != 'c' and orden != 'n':
                print("Opcion no valida, por favor  ingrese (c) para calificacion o (n) para nombre.")
                orden = input("Ingrese  para mostrar en orden (c) para calificacion o (n) para nombre: ").lower()       
           
            if resultados:
               if orden == 'c':
                    resultados.sort(key=lambda p: p.calificacion, reverse=True)
                    for proveedores in resultados:
                        print(proveedores)
               if orden == 'n':
                    resultados.sort(key=lambda p: p.nombre.lower())
                    for proveedores in resultados:
                        print(proveedores)
            else:
                print(f"No se encontraron proveedores que ofrezcan:  {servicio}")

        elif opcion == "3":
            print(" Mostrar proveedores por nombre ")
            proveedores = tree.obtener_proveedores() 
            proveedores.sort(key=lambda p: p.nombre.lower()) # esto lo puse para ordenar los nombres alfabéticamente
            for p in proveedores:
                print(f"Nombre: {p.nombre} - Servicio: {p.tipo_servicio} - Calificación: {p.calificacion}⭐ ")

        elif opcion == "4":
            print("\n--- Mostrar proveedores por calificación ---")
            print("Proveedores desde el mejor al peor:")
            proveedores = tree.obtener_proveedores()
            proveedores.sort(key=lambda p: p.calificacion, reverse=True)

            for p in proveedores:
                print(f"Nombre: {p.nombre} - Servicio: {p.tipo_servicio} - Calificación: {p.calificacion}⭐ ")

        elif opcion == "5":
            print("Gracias por usar el programa")
            break