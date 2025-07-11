class Estudiante:
    def __init__(self, nombre, carne, carrera, nota):
        self.nombre = nombre
        self.carne = carne
        self.carrera = carrera
        self.nota = nota
    def informacion(self):
        print(f"El estudiante {self.nombre} de la carrera: {self.carrera} que se identifica con el carné: {self.carne} su nota es : {self.nota}")
Estudiantes = []
while True:
    print("1. Ingresar a un nuevo estudiante")
    print("2. Buscar estudiante por su carné")
    print("3. Promedio de todos los estudiantes ingresados")
    print("4. SALIR")
    opcion = int(input("Seleccione una opcion: "))
    match opcion:
        case 1:
            nombre = input("Ingrese el nombre: ")
            carne = input("Ingrese el carne: ")
            carrera = input("Ingrese el carrera: ")
            nota = input("Ingrese el nota final del estudiante: ")
            nuevoEstudiante = Estudiante(nombre, carne, carrera, nota)
            Estudiantes.append(nuevoEstudiante)
            break
        case 2:
            buscarEstudiante = input("Ingrese el carné del estudiante que desea buscar: ")
            for estudiante in Estudiantes:
                if buscarEstudiante == estudiante.carne:
                    estudiante.informacion()
            break
