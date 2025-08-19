from math import ceil
from .nodo import Node
class BTree:
    def __init__(self, m):
        self.order = m
        self.t = ceil(m / 2)  # grado mínimo calculado
        self.root = Node(self.t, True)

    def insert(self, key):
        root = self.root

        if root.is_full():
            # Lleno, necesitamos dividir
            new_root = Node(self.t, False)
            new_root.children.append(root)
            new_root.split_child(0)

            # Determinar en que hijo insertar la nueva clave
            i = 0
            if key > new_root.keys[0]:
                i += 1
            new_root.children[i].insert_non_full(key)

            self.root = new_root
        else:
            root.insert_non_full(key)

    def traverse_inorder(self):
        print("Recorrido inorden:")
        self.root.traverse_inorder()
        print()

    def obtener_proveedores(arbol):
        lista = []

        def recorrer(nodo):
            for i in range(len(nodo.keys)):
                if not nodo.leaf:
                    recorrer(nodo.children[i])
                lista.append(nodo.keys[i])  
            if not nodo.leaf:
                recorrer(nodo.children[-1])

        recorrer(arbol.root)
        return lista

