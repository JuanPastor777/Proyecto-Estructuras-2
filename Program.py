from Arbol.Arbol import BTree
from Clases.Proveedores import Proveedor
if __name__ == "__main__":
    tree = BTree(4)
    proveedores = []  # almacena provvedores

    while True:
        print("     MENu PARa GESTIoN DE PROVEEDORES  ")
        print(" 1. Registrar proveedor               ")
        print(" 2. Buscar por tipo de servicio       ")
        print(" 3. Mostrar proveedores por nombre    ")
        print(" 4. Mostrar proveedores por calificaciion ")
        print(" 5. Salir ")

        opcion = input("selecciona una opcion: ")

        if opcion == "1":
            print(" Registro de nuevo proveedor ")
            try:
                id_trabajador = int(input("Ingrese el ID: "))
                # esto verifica si el ID existe
                existe = False
                for p in proveedores:
                    if p["id"] == id_trabajador:
                        existe = True
                        break
                if existe:
                    print("Ya existe un proveedor con este ID, puede intebtar con otro.")
                    continue

                nombre = input("Nombre del trabajador: ")
                tipo_servicio = input("Tipo de servicio: ")
                calificacion = int(input("calificacion de 1 o 5 estrellas: "))
                
                if calificacion < 1 or calificacion > 5:
                    print(" la calificacion debe de ser entre 1 y 5.")
                    continue

                proveedor = {
                    "id": id_trabajador,
                    "nombre": nombre,
                    "servicio": tipo_servicio,
                    "calificacion": calificacion
                }

                proveedores.append(proveedor)
                tree.insert(id_trabajador)  # esto es para insertar solo el ID en el árbol

                print("El Proveedor se registro correctamente.")
            except ValueError:
                print(" ingresa un vaor que sea valido.")


        elif opcion == "5":
            print("Gracias por usar el programa")
            break
      