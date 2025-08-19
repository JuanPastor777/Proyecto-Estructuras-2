from Arbol.Arbol import BTree
from Clases.Proveedores import Proveedor

if __name__ == "__main__":
    # Árbol B donde la clave será el ID y el valor el objeto Proveedor completo
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
                calificacion = int(input("Calificación (1 a 5 estrellas): "))

                if calificacion < 1 or calificacion > 5:
                    print("⚠️ La calificación debe ser entre 1 y 5.\n")
                    continue

                # Crear el objeto Proveedor (el ID se genera automáticamente)
                nuevo_proveedor = Proveedor(nombre, tipo_servicio, calificacion)
                
                # Insertar en el árbol B (clave=ID, valor=objeto Proveedor completo)
                tree.insert(nuevo_proveedor)

                print(f"✅ Proveedor registrado correctamente con ID {nuevo_proveedor.id}")
                print(f"Datos almacenados: {nuevo_proveedor.__dict__}\n")

            except ValueError:
                print("⚠️ Ingresa un valor válido.\n")
        elif opcion == "2":
            servicio = input("Ingrese el tipo de servicio a buscar: ")
            resultados = tree.search_by_service(servicio)
            if resultados:
                print(f"\nProveedores que ofrecen: {servicio}:")
                for proveedor in resultados:
                    print(proveedor)
            else:
                print(f"No se encontraron proveedores que ofrezcan '{servicio}'.")

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