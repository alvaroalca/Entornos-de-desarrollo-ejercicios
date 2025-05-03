class Libro:
    def __init__(self, isbn, titulo, anio_publicacion):
        self.isbn = isbn
        self.titulo = titulo
        self.anio_publicacion = anio_publicacion
        self.estado = "disponible"  
        self.autores = [] # lista de autores, de momento vacio

    def prestar(self):
        if self.estado == "disponible":
            self.estado = "prestado"
            return f"Libro '{self.titulo}' prestado."
        else:
            return f"Libro '{self.titulo}' ya está prestado."

    def devolver(self):
        if self.estado == "prestado":
            self.estado = "disponible"
            return f"Libro '{self.titulo}' devuelto."
        else:
            return f"Libro '{self.titulo}' ya está disponible."

    def agregar_autor(self, autor):
        if autor not in self.autores:
            # evitamos un duplicado con el if
            self.autores.append(autor)

    def mostrar_info(self):
        # mostramos información del libro y  sus autores y lo dejamos bien escrito
        # para que se vea bien en la salida
        autores_str = ", ".join(self.autores)
        return f"'{self.titulo}' ({self.anio_publicacion}) - Autores: {autores_str}, Estado: {self.estado}"


class Autor:
    def __init__(self, nombre, nacionalidad):
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.libros = []
    
    

    def escribir_libro(self, libro):
        if libro not in self.libros:
            # evitamos un duplicado con el if
            self.libros.append(libro)
            libro.agregar_autor(self.nombre)


class Biblioteca:
    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion
        # Inicializamos la lista de libros como vacia
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def remover_libro(self, isbn):
        libro_a_remover = None
        for libro in self.libros:
            if libro.isbn == isbn:
                libro_a_remover = libro
                break
        if libro_a_remover:
            self.libros.remove(libro_a_remover)
            return print(f"El libro con ISBN {isbn} ha sido removido.")
        else:
            return print(f"No se encontró un libro con el ISBN {isbn}.")

    def listar_libros(self):
        if not self.libros:
            return "No hay libros en la biblioteca."
        return "\n".join(libro.mostrar_info() for libro in self.libros)
    


# estos son los ejemplos de los usos que vamos a dar:

# creamos autores
autor1 = Autor("Álvaro Alcaraz Pérez", "Español")
autor2 = Autor("Brandon Sanderson", "Americano")

# creamos libros
libro1 = Libro("2222222", "Teo va a la escuela", 2000)
libro2 = Libro("1234", "Elantris", 2005)

# hacemos que los autores escriban libros y algun autor hace un libro en comun
autor1.escribir_libro(libro1)
autor2.escribir_libro(libro2)
autor1.escribir_libro(libro2)

# creamos la biblioteca
biblioteca = Biblioteca("Biblioteca UAX", "Calle de la Universidad, 1")

# agregamos libros a biblioteca
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)

# listamos libros de la biblioteca
print("Libros en la biblioteca:")
print(biblioteca.listar_libros())
print()

# hacemos un par de prestamos y devoluciones
print("vamos a prestar y devolver libros:")
print(libro1.prestar())
print(libro1.prestar())  # provamos error
print(libro1.devolver())

print()
# borramos algun libro de la biblioteca y probamos un libro que no existe tambien
biblioteca.remover_libro("1234")
print()
print("intentando borrar un libro que no existe:")
biblioteca.remover_libro("9999")

# vemos la lista despues de borrar
print("\nLibros en la biblioteca después de eliminar:")
print(biblioteca.listar_libros())
