class ColaDoblementeCircular:

    def __init__(self):
        self.cabeza = None
        self.cola = None

    class Nodo:
        def __init__(self, dato):
            self.dato = dato
            self.siguiente = None
            self.anterior = None

    def insertar(self, dato):
        nuevo_nodo = self.Nodo(dato)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
            self.cabeza.anterior = self.cola
            self.cola.siguiente = self.cabeza
        else:
            nuevo_nodo.siguiente = self.cabeza
            nuevo_nodo.anterior = self.cola
            self.cabeza.anterior = nuevo_nodo
            self.cola.siguiente = nuevo_nodo
            self.cabeza = nuevo_nodo
        self.mostrar_movimientos("Inserción", dato)

    def eliminar(self):
        if not self.cabeza:
            print("La cola está vacía.")
            return
        eliminado = self.cola.dato
        if self.cabeza == self.cola:
            self.cabeza = None
            self.cola = None
        else:
            self.cola = self.cola.anterior
            self.cola.siguiente = self.cabeza
            self.cabeza.anterior = self.cola
        self.mostrar_movimientos("Eliminación", eliminado)
        return eliminado

    def mostrar_movimientos(self, accion, dato):
        print(f"{accion}: {dato}")
        actual = self.cabeza
        if actual is None:
            print("Cola vacía")
            return
        print("Cola:")
        while True:
            print(actual.dato)
            actual = actual.siguiente
            if actual == self.cabeza:
                break
