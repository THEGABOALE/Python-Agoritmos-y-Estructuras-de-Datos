class Estudiante:
    def __init__(self,ID,Nombre,Carrera,Nota_Final):
        self.ID=ID
        self.Nombre=Nombre
        self.Carrera=Carrera
        self.Nota_Final=Nota_Final
        
    def __str__(self):
        return f"ID: {self.ID}, Nombre: {self.Nombre}, Carrera: {self.Carrera}, Nota Final: {self.Nota_Final}"
        
class Nodoarbol:
    def __init__(self,estudiante):
        self.estudiante=estudiante
        self.izquierda=None
        self.derecha=None
        
class Arbolbinariobusqueda:
    def __init__(self):
        self.raiz=None
        
    def insertar(self, estudiante):
        nuevo_nodo: Nodoarbol = Nodoarbol(estudiante)
        if self.raiz is None:
            self.raiz = nuevo_nodo
            return
        self.insertar_aux(self.raiz, nuevo_nodo)
    
    def insertar_aux(self, actual, nuevo_nodo):
        if nuevo_nodo.estudiante.ID < actual.estudiante.ID:
            if actual.izquierda is None:
                actual.izquierda = nuevo_nodo
            else:
                self.insertar_aux(actual.izquierda, nuevo_nodo)
        else:
            if actual.derecha is None:
                actual.derecha = nuevo_nodo
            else:
                self.insertar_aux(actual.derecha, nuevo_nodo)
                
    def buscar(self, ID):
        pass
    
    def aux_buscar(self, ID):
        pass
    
    def recorrer_inorden(self):
        self.aux_inorden(self.raiz)
        
    def aux_inorden(self, nodo):
        if nodo is not None:
            self.aux_inorden(nodo.izquierda)
            print(nodo.estudiante)
            self.aux_inorden(nodo.derecha)
    
    def eliminar(self, estudiante):
        self.raiz = self.aux_eliminar(self.raiz, estudiante)
        
    def aux_eliminar(self, actual, estudiante):
        if not actual:
            print("El arbol está vacío")
            return
        elif estudiante < actual.estudiante.ID:
            actual.izquierda = self.aux_eliminar(actual.izquierda, estudiante)
        elif estudiante > actual.estudiante.ID:
            actual.derecha = self.aux_eliminar(actual.derecha, estudiante)
        else:
            #Caso1
            if not actual.izquierda and not actual.derecha:
                return None
            #Caso 2
            elif not actual.derecha:
                return actual.izquierda
            elif not actual.izquierda:
                return actual.derecha
            #Caso 3
            else:
                sucesor = self.buscar_sucesor(actual.derecha)
                actual.estudiante.ID = sucesor.estudiante
                actual.derecha = self.aux_eliminar(actual.derecha, sucesor.estudiante)
    
    def buscar_sucesor(self, nodo) -> any:
        actual = nodo
        while actual.izquierda:
            actual = actual.izquierda
        return actual

Estudiantes = {
    Estudiante(1, "Gabriel", "Sistemas", 90),
    Estudiante(2, "Joha", "Industrial", 70),
    Estudiante(3, "Nicolas", "Diseño", 60),
    Estudiante(4, "Valeria", "Marketing", 80)
}

cl = Arbolbinariobusqueda()

for est in Estudiantes:
    cl.insertar(est)

print("-----Recorrido en Inorden----")
cl.recorrer_inorden()
