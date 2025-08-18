from collections import deque
class Node:
    def __init__(self, t, leaf=False):
        self.t = t  # grado mínimo
        self.leaf = leaf
        self.keys = []  # claves
        self.children = []  # referencias a hijos


    def is_full(self):
        return len(self.keys) == (2 * self.t) - 1

    def insert_non_full(self, key):
        i = len(self.keys) - 1

        if self.leaf:
            # Insertar en nodo hoja
            self.keys.append(None)  # Espacio temporal
            while i >= 0 and key < self.keys[i]:
                self.keys[i + 1] = self.keys[i]
                i -= 1
            self.keys[i + 1] = key
        else:
            # Encontrar el hijo adecuado para la clave
            while i >= 0 and key < self.keys[i]:
                i -= 1
            i += 1

            # Si el hijo est lleno dividirlo
            if self.children[i].is_full():
                self.split_child(i)
                if key > self.keys[i]:
                    i += 1

            # Insertar recursivamente en el hijo adecuado
            self.children[i].insert_non_full(key)

    def split_child(self, i):
        t = self.t
        y = self.children[i]
        z = Node(t, y.leaf)

        # La clave media que subira al padre
        mid_key = y.keys[t - 1]

        # Dividir las claves
        z.keys = y.keys[t:(2 * t - 1)]
        y.keys = y.keys[0:(t - 1)]

        # Si no es hoja, dividir los hijos
        if not y.leaf:
            z.children = y.children[t:(2 * t)]
            y.children = y.children[0:t]

        # Insertar el nuevo nodo en los hijos del padre
        self.children.insert(i + 1, z)
        # Insertar la clave media en el padre
        self.keys.insert(i, mid_key)

    def traverse_inorder(self):
        for i in range(len(self.keys)):
            if not self.leaf:
                self.children[i].traverse_inorder()
            print(self.keys[i], end=' ')
        if not self.leaf:
            self.children[-1].traverse_inorder()

    def collect_levels(self):
        result = []
        queue = deque([(self, 0)])
        while queue:
            node, level = queue.popleft()
            if len(result) <= level:
                result.append([])
            result[level].append(node)
            for child in node.children:
                queue.append((child, level + 1))
        return result

